class Utils:
    def __init__(self) -> None:
        pass

    def format_time(self, time: int) -> list[str, str, str]:
        time_ = time // 1000
        sec = time_ % 60
        temp_ = time_ // 60
        minute = temp_ % 60
        temp_ = temp_ // 60
        hour = temp_ % 60
        new_time = [hour, minute, sec, time]

        for i in range(len(new_time)):
            if new_time[i] < 10:
                new_time[i] = f"0{str(new_time[i])}"
            else:
                new_time[i] = str(new_time[i])

        format_time = f"{new_time[0]}:{new_time[1]}:{new_time[2]}"
        return format_time
