# **YouTube Video Summarizer and Multilingual Text-to-Speech Converter**

- This project leverages **OpenAI Whisper**, **Google Translator**, and **gTTS (Google Text-to-Speech)** to automatically summarize YouTube videos, translate the summary into various languages, and convert the translated text into speech. The model adapts based on the content of the video, making it versatile for any video genre or topic.

## **Features**
- **YouTube to Text**: Extract audio from any YouTube video and convert it into text using OpenAI Whisper.
- **Dynamic Summarization**: Automatically generates summaries based on the video’s content, whether it's educational, entertainment, or other genres.
- **Multilingual Support**: Translate the summarized text into any language supported by Google Translator.
- **Text-to-Speech Conversion**: Convert the translated text into speech using gTTS, allowing you to listen to the summary on the go.
  
## **How It Works**
1. **Extract Video Audio**: Provide a YouTube link, and the audio will be extracted from the video.
2. **Generate Summary**: The content is summarized automatically using a large language model (GPT-3.5-turbo).
3. **Translate Summary**: The summary is translated into the target language of your choice.
4. **Convert to Speech**: The translated summary is converted into speech, and an audio file is generated.

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-link>
