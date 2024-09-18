# Voice Cloning Project with Bark and HuBERT

## Project Description

Voice cloning is a technology that allows the creation of digital replicas of a human voice, faithfully reproducing characteristics such as timbre, intonation, and speaking style. This project leverages advanced models like **Bark** for voice synthesis and **HuBERT** for audio feature analysis.

Using deep learning techniques, voice cloning can generate speech that mimics a specific speaker from a limited voice sample. The project can be applied in various fields, including:
- Dubbing generation for media
- Creating voices for virtual assistants
- Customizing audio content

However, this type of technology raises ethical concerns, especially regarding data privacy and the authenticity of voice samples.

## Creators

This project was developed by **Samy Hadj-Said**, **Jason Perez**, and **Briac Six**.

## Demonstration

You can view the full demonstration on Google Colab by following [this link](https://colab.research.google.com/drive/1kRR49HINV5_EeorFLMiMd9AeQm--gfmX?usp=sharing).

## Installation

To run this project, you will need to install the following libraries:
- bark-voice-cloning-HuBERT-quantizer
- bark

## Usage

1. **Loading Bark and HuBERT Models**: Load the required models for audio generation and manipulation.
2. **Audio Generation from Text**: Generate an audio file from the provided text input.
3. **Preparing Audio for Cloning and Model Setup**: Set up the models and prepare the audio for cloning.
4. **Semantic Token Extraction with HuBERT**: Extract semantic tokens from the audio using the HuBERT model.
5. **Audio Generation with Cloned Voice**: Use the extracted tokens to generate an audio file with the cloned voice.

## Key Files

- `bark-voice-cloning-HuBERT-quantizer`: Model for semantic token extraction with HuBERT.
- `bark`: Model for voice synthesis.
- `audio.wav`: Example of audio to be cloned.
- `output.npz`: File containing the generated prompts for audio generation.

## References and Documentation

- [Bark GitHub Repository](https://github.com/serp-ai/bark-with-voice-clone)
- [HuBERT GitHub Repository](https://github.com/gitmylo/bark-voice-cloning-HuBERT-quantizer)
- [Coqui TTS](https://github.com/coqui-ai/TTS)

## Ethical Concerns

While voice cloning technology is fascinating and opens up many possibilities, it raises important ethical concerns, particularly regarding the authenticity of voices and the protection of personal data. It is essential to use these technologies responsibly.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
