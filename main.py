import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json

with open("players.json", "r") as read_file:
    players = json.load(read_file)


def main() -> None:
    for nickname, data in players.items():
        race, _ = Race.objects.get_or_create(
            name=data["race"]["name"],
            description=data["race"]["description"]
        )
        guild_data = data.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                description=guild_data["description"]
            )
        else:
            guild = None
        for skill_data in data["race"]["skills"]:
            skill, _ = Skill.objects.get_or_create(
                name=skill_data["name"],
                bonus=skill_data["bonus"],
                race=race)
        player, _ = Player.objects.get_or_create(
            nickname=nickname,
            email=data["email"],
            bio=data["bio"],
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
