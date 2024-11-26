from moviepy.editor import TextClip, concatenate_videoclips

def create_video(words):
    clips = []

    for word in words:
        text = f"Word: {word['word']}\nMeaning: {word['meaning']}\nExample: {word['example']}"
        clip = TextClip(text, fontsize=70, color='white', size=(1280,720), bg_color='black', duration=5)
        clips.append(clip)
    
    final_video = concatenate_videoclips(clips)
    final_video.write_videofile("daily_german_words.mp4", fps=24)

words = [
    {"word": "Haus", "meaning": "House", "example": "Das Haus ist groß."},
    {"word": "Apfel", "meaning": "Apple", "example": "Ich esse einen Apfel."},
]

create_video(words)