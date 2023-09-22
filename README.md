# RagaCraft

RagaCraft is an innovative application designed to democratize the rich and emotive world of Indian classical music's Ragas. It enables users, irrespective of their musical knowledge, to experience the therapeutic benefits of Ragas by generating Raga-based music tailored to their emotions.

## Overview
Our application is empowered by the Audiocraft library and is meticulously developed using Streamlit, ensuring a seamless and user-friendly experience. It is deployed on AWS EC2, optimizing performance and scalability. The core idea is to enhance the accessibility of the therapeutic and aesthetic essence of Indian classical music, making it a universal experience.

[Live App](http://18.188.244.79:8501)

## Features
- **User-Friendly Interaction**: Users can input their mood, and the app curates personalized Raga-based music.
- **Emotion-Centric Generation**: The app crafts music that resonates with the user’s emotional state, leveraging the diversity of Ragas.
- **Therapeutic Accessibility**: It opens up the therapeutic realm of Indian classical music to everyone.

## Demonstrations
- [Pitch Deck](https://pitch.com/public/7323c1c4-2eb1-48cf-9af6-e9c3da5e0a1c)
- [Presentation](https://youtu.be/9G7hagBrbgE)
- [App Demo](https://youtu.be/KFGr0pkR1wE)

## Technology Stack
- **Streamlit**: For building the web application.
- **AWS EC2**: Deployment platform, chosen for its scalability and resource management capabilities.
- **JavaScript**: Utilized for selecting the appropriate raga based on user input.
- **OpenAI LLM**: Empowers the app to design prompts for music generation based on user’s emotional input.

## How it Works
1. **Customer Input**: The user provides their emotional state.
2. **Raga Selection**: JavaScript is employed to select the appropriate raga.
3. **Prompt Generation**: A request is sent to the API, and the generated prompt is forwarded to Audiogen.
4. **Music Generation**: Audiogen processes the prompt to produce a song, which is then delivered back to the user.

## Future Developments
We aim to refine the quality of the produced Raga music by utilizing a dedicated Raga dataset to fine-tune the Audiocraft model, ensuring the production of high-quality Raga music.

## Running the Code
To run the code, use the following command:
```shell
streamlit run app.py
```

## Acknowledgments

We extend our gratitude to everyone who supported us in this endeavor, especially to the contributors and maintainers of the utilized libraries and platforms. Our journey in bridging the gap between the diverse world of Ragas and everyday users continues, and we are excited about the possibilities ahead.

## License

This project is not open-source, and need to attain a license to use this code.

## Contact

For any queries or discussions related to RagaCraft, please feel free to contact us.
