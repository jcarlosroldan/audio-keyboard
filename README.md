# Wireless keyboard

The goal of this project is to train a LSTM model that, listening to the microphone at real time, simulates the keystrokes it hears in the keyboard for you.

It is composed of three scripts:

1. callibrate.py: records you microphone and keystrokes for 10 seconds and stores it in recordings incrementally.
2. train.py: loads the recordings and trains a LSTM model to predict them.
3. use.py: uses the trained model to simulate keystrokes on real time.

## Installation

Just clone this repository and run `pip install -r requirements.txt`. Then you can use the three files.

## Development

This is on a _very_ early stage: only the callibrate script is already finihed. The next steps are:

1. Build and train the model in train.py.
2. Write the keystroke simulator that runs the prediction on real time.

Feel free to complete any of those.

## Notes

The recording format is a dictionary of `{input: np.array, "output': np.array]`. Input is a spectrogram of the microphone with shape 387 x 1136 x 2 (frame x frequency x stereo_ear). Output has shape 387 x 253 (frame x keys) where the keys are indexed by [virtual key](https://cherrytree.at/misc/vk.htm) and each value is 1 when the stroke is pressed, -1 when the stroke is released, 0 otherwise.