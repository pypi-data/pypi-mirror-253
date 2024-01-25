#include <tuple>
#include <vector>
#include <cmath>
#include <chrono>
#include <iostream>

#include <nanobind/nanobind.h>
#include <nanobind/stl/tuple.h>
#include <nanobind/stl/vector.h>

namespace nb = nanobind;

struct Vec2
{
	Vec2(float x, float y) : x(x), y(y) {}

	float x, y;

	float distanceSquared(const Vec2& other)
	{
		return std::pow(x - other.x, 2) + std::pow(y - other.y, 2);
	}
};

struct Chunk
{
	Chunk(Vec2 position, int64_t id, float maxLength) : tl(position), tr(position.x + maxLength, position.y), br(position.x + maxLength, position.y + maxLength), bl(position.x, position.y + maxLength) , id(id) {}

	Vec2 tl, tr, br, bl;
	std::vector<std::pair<Vec2, Vec2>*> walls;

	int64_t id;
};

class CollisionHandler 
{
public:
	CollisionHandler() : cpID(0), maxLength(0.0) {}

	void uploadData(std::vector<std::tuple<float, float>> inner, std::vector<std::tuple<float, float>> outer, std::vector<std::tuple<float, float>> checkpoints, float maxLength)
	{
		for (size_t i = 0; i < inner.size() - 1; ++i)
		{
			walls.push_back(std::make_pair(Vec2(std::get<0>(inner[i]), std::get<1>(inner[i])), Vec2(std::get<0>(inner[i + 1]), std::get<1>(inner[i + 1]))));
		}

		walls.push_back(std::make_pair(Vec2(std::get<0>(inner.back()), std::get<1>(inner.back())), Vec2(std::get<0>(inner[0]), std::get<1>(inner[0]))));

		for (size_t i = 0; i < outer.size() - 1; ++i)
		{
			walls.push_back(std::make_pair(Vec2(std::get<0>(outer[i]), std::get<1>(outer[i])), Vec2(std::get<0>(outer[i + 1]), std::get<1>(outer[i + 1]))));
		}

		walls.push_back(std::make_pair(Vec2(std::get<0>(outer.back()), std::get<1>(outer.back())), Vec2(std::get<0>(outer[0]), std::get<1>(outer[0]))));

		for (size_t i = 0; i < checkpoints.size() - 1; i += 2)
		{
			this->checkpoints.push_back(std::make_pair(Vec2{ std::get<0>(checkpoints[i]), std::get<1>(checkpoints[i]) }, Vec2{ std::get<0>(checkpoints[i + 1]), std::get<1>(checkpoints[i + 1]) }));
		}

		cpID = 0;

		this->maxLength = maxLength;

		generateChunks();
	}

	void generateChunks()
	{
		float max_x = 3360, max_y = 1890;
		gridWidth = (max_x / maxLength) + 1;
		gridHeight = (max_y / maxLength) + 1;

		for (float y = 0.0; y < max_y; y += maxLength)
		{
			for (float x = 0.0; x < max_x; x += maxLength)
			{
				generateChunk(Vec2(x, y));
			}
		}
	}

	void generateChunk(Vec2 position)
	{
		chunks.push_back(Chunk(position, getChunkIndex(position), maxLength));
		for (auto& it : walls)
		{
			if (isWallInChunk(&chunks.back(), it))
			{
				chunks.back().walls.push_back(&it);
			}
		}
	}

	bool isWallInChunk(Chunk* chunk, std::pair<Vec2, Vec2> wall)
	{
		return isPointInRectangle(wall.first, chunk->tl, maxLength) ||
			isPointInRectangle(wall.second, chunk->tl, maxLength) ||
			areLinesIntersecting(wall, std::make_pair(chunk->tl, chunk->tr)) ||
			areLinesIntersecting(wall, std::make_pair(chunk->tr, chunk->br)) ||
			areLinesIntersecting(wall, std::make_pair(chunk->br, chunk->bl)) ||
			areLinesIntersecting(wall, std::make_pair(chunk->bl, chunk->tl));
	}

	bool isPointInRectangle(Vec2 point, Vec2 position, float length)
	{
		return point.x >= position.x &&
			point.x <= position.x + length &&
			point.y >= position.y &&
			point.y <= position.y + length;
	}

	bool areLinesIntersecting(std::pair<Vec2, Vec2> wall, std::pair<Vec2, Vec2> boundary)
	{
		const auto [uA, uB] = calculateCollisionFactor(wall.first, wall.second, boundary.first, boundary.second);

		return (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1);
	}

	int32_t getChunkIndex(Vec2 point)
	{
		return (int)(point.x / maxLength) + (int)(point.y / maxLength) * gridWidth;
	}

	Chunk* getChunk(Vec2 point)
	{
		size_t index = getChunkIndex(point);

		if (index < chunks.size() && index >= 0)
		{
			return &chunks[index];
		}
		else
		{
			return nullptr;
		}
	}

	/*
	* return tuple of <List Collision Points, Player alive, Checkpoint hit>
	*/
	std::tuple<std::vector<std::tuple<float, float, float>>, bool, bool> calculateCollisionPoints(std::vector<std::tuple<float, float>> rayPoints, std::tuple<float, float> center, std::vector<std::tuple<float, float>> hitbox)
	{
		Vec2 cp{ std::get<0>(center), std::get<1>(center) };
		std::vector<std::tuple<float, float, float>> results;
		results.reserve(rayPoints.size());
		bool playerHit = false;

		Chunk* chunk = getChunk(cp);

		for (auto& rp : rayPoints)
		{
			Vec2 point{ std::get<0>(rp), std::get<1>(rp) };
			Vec2 rayPoint{ std::get<0>(rp), std::get<1>(rp) };
			std::pair<Vec2, Vec2>* w = nullptr;
			float distance = maxLength * maxLength;

			if (chunk != nullptr)
			{
				for (auto& wall : chunk->walls)
				{
					Vec2 temp = calculateCollisionPoint(cp, rayPoint, wall->first, wall->second);

					if (cp.distanceSquared(temp) < distance)
					{
						point = temp;
						distance = cp.distanceSquared(temp);
						w = wall;
					}

					for (size_t i = 0; i < 3; ++i)
					{
						const auto [uA, uB] = calculateCollisionFactor(Vec2(std::get<0>(hitbox[i]), std::get<1>(hitbox[i])), Vec2(std::get<0>(hitbox[i + 1]), std::get<1>(hitbox[i + 1])), wall->first, wall->second);
						if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1)
						{
							playerHit = true;
							cpID = 0;
						}
					}

					const auto [uA, uB] = calculateCollisionFactor(Vec2(std::get<0>(hitbox[3]), std::get<1>(hitbox[3])), Vec2(std::get<0>(hitbox[0]), std::get<1>(hitbox[0])), wall->first, wall->second);
					if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1)
					{
						playerHit = true;
						cpID = 0;
					}
				}

				if (w == nullptr)
				{
					for (auto& chunk : chunks)
					{
						if (isPointInRectangle(rayPoint, chunk.tl, maxLength))
						{
							for (auto& wall : chunk.walls)
							{
								Vec2 temp = calculateCollisionPoint(cp, rayPoint, wall->first, wall->second);

								if (cp.distanceSquared(temp) < distance)
								{
									point = temp;
									distance = cp.distanceSquared(temp);
									w = wall;
								}
							}
						}
						else if (areLinesIntersecting(std::make_pair(cp, rayPoint), std::make_pair(chunk.tl, chunk.tr)) ||
							areLinesIntersecting(std::make_pair(cp, rayPoint), std::make_pair(chunk.tr, chunk.br)) ||
							areLinesIntersecting(std::make_pair(cp, rayPoint), std::make_pair(chunk.br, chunk.bl)) ||
							areLinesIntersecting(std::make_pair(cp, rayPoint), std::make_pair(chunk.bl, chunk.tl)))
						{
							for (auto& wall : chunk.walls)
							{
								Vec2 temp = calculateCollisionPoint(cp, rayPoint, wall->first, wall->second);

								if (cp.distanceSquared(temp) < distance)
								{
									point = temp;
									distance = cp.distanceSquared(temp);
									w = wall;
								}
							}
						}
					}
				}
			}

			results.push_back(std::make_tuple(point.x, point.y, std::sqrt(distance)));
		}

		bool cpHit = false;

		for (size_t i = 0; i < 3; ++i)
		{
			const auto [uA, uB] = calculateCollisionFactor(Vec2(std::get<0>(hitbox[i]), std::get<1>(hitbox[i])), Vec2(std::get<0>(hitbox[i + 1]), std::get<1>(hitbox[i + 1])), checkpoints[cpID].first, checkpoints[cpID].second);
			if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1)
			{
				cpID++;
				cpHit = true;

				if (cpID == checkpoints.size())
				{
					cpID = 0;
				}
			}
		}

		const auto [uA, uB] = calculateCollisionFactor(Vec2(std::get<0>(hitbox[3]), std::get<1>(hitbox[3])), Vec2(std::get<0>(hitbox[0]), std::get<1>(hitbox[0])), checkpoints[cpID].first, checkpoints[cpID].second);
		if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1)
		{
			cpID++;
			cpHit = true;

			if (cpID == checkpoints.size())
			{
				cpID = 0;
			}
		}

		return std::make_tuple(results, playerHit, cpHit);
	}

	std::tuple<float, float> calculateCollisionFactor(Vec2 a1, Vec2 a2, Vec2 b1, Vec2 b2)
	{
		if ((((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y)) == 0) || (((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y)) == 0))
		{
			float uA = -1.0;
			float uB = -1.0;
			return std::make_tuple(uA, uB);
		}

		float uA = ((b2.x - b1.x) * (a1.y - b1.y) - (b2.y - b1.y) * (a1.x - b1.x)) /
			((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y));
		float uB = ((a2.x - a1.x) * (a1.y - b1.y) - (a2.y - a1.y) * (a1.x - b1.x)) /
			((b2.y - b1.y) * (a2.x - a1.x) - (b2.x - b1.x) * (a2.y - a1.y));

		return std::make_tuple(uA, uB);
	}

	Vec2 calculateCollisionPoint(Vec2 a1, Vec2 a2, Vec2 b1, Vec2 b2)
	{
		const auto [uA, uB] = calculateCollisionFactor(a1, a2, b1, b2);

		if (uA >= 0 && uA <= 1 && uB >= 0 && uB <= 1)
		{
			return Vec2(a1.x + (uA * (a2.x - a1.x)), a1.y + (uA * (a2.y - a1.y)));
		}
		else
		{
			return Vec2(INFINITY, INFINITY);
		}
	}

private:
	std::vector<std::pair<Vec2, Vec2>> walls, checkpoints;
	std::vector<Chunk> chunks;

	uint16_t cpID, gridWidth, gridHeight;

	float maxLength;

};

NB_MODULE(collision, m) {
	nb::class_<CollisionHandler>(m, "CollisionHandler")
		.def(nb::init<>())
		.def("uploadData", &CollisionHandler::uploadData)
		.def("calculateCollisionPoints", &CollisionHandler::calculateCollisionPoints)
		.def("calculateCollisionPoint", &CollisionHandler::calculateCollisionPoint)
		.def("calculateCollisionFactor", &CollisionHandler::calculateCollisionFactor);
}