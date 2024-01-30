def age_assignment(*names: str, **ages_info: int) -> str:
    matched_ages = (
        f"{name} is {ages_info[name[0]]} years old."
        for name in sorted(names)
    )

    return "\n".join(matched_ages)
