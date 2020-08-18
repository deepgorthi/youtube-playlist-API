from datetime import timedelta

class YoutubePlaylistDuration:

    def __init__(self, hours, minutes, seconds):
        # self.video_id = video_id
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def getDuration(self):
        return self.hours, self.minutes, self.seconds

    # def getDurationSeconds(self):
    #     return self.video_id, (self.hours*60*60)+(self.minutes*60)+self.seconds

    def getDurationSeconds(self):
        duration_seconds = timedelta(
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds
        ).total_seconds()
        return duration_seconds