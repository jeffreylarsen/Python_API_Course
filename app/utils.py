from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def calculate_reading_time(sentence, words_per_minute):
    words = len(sentence.split())
    reading_time_minutes = words / words_per_minute
    reading_time_seconds = reading_time_minutes * 60

    hours = int(reading_time_seconds // 3600)
    minutes = int((reading_time_seconds % 3600) // 60)
    seconds = int(reading_time_seconds % 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Example usage
sentence = "This is a sample sentence that we want to calculate the reading time for."
words_per_minute = 200  # Adjust this value according to the expected reading speed

reading_time = calculate_reading_time(sentence, words_per_minute)
print("Reading Time:", reading_time)
