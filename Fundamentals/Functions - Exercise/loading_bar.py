def loading_bar(progress: int) -> str:
    if progress == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{progress}% [{'%' * (progress // 10)}{'.' * (10 - progress // 10)}]\nStill loading..."
    
    
progress = int(input())
print(loading_bar(progress))