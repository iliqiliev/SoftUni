class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(
        self, course_name: str, language: str, skill_earned: int
    ) -> str:
        
        if language != self.language:
            return f"{self.name} does not know {language}"

        self.skills += skill_earned
        
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language: str, skill_needed: int) -> str:
        if new_language == self.language:
            return f"{self.name} already knows {new_language}"

        if skill_needed > self.skills:
            missing_skills = skill_needed - self.skills
            return f"{self.name} needs {missing_skills} more skills"

        old_language = self.language
        self.language = new_language
        return f"{self.name} switched from {old_language} to {new_language}"
