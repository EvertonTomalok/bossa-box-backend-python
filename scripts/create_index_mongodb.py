from src.adapters.mongodb.db import MongoDBDatabase


def create_index():
    with MongoDBDatabase("tools", "tools_collection") as db:
        db.create_index(
            [("tags", 1)],
            "tags_index",
        )


if __name__ == "__main__":
    print("Starting!")
    create_index()
    print("Done!")
