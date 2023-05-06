import sys
import os
from pydub import AudioSegment
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QTextEdit


def convert_seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours:02d}{minutes:02d}{seconds:02d}'


class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Audio File Trimmer')

        layout = QVBoxLayout()

        self.file_input = QLineEdit()
        layout.addWidget(self.file_input)

        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browse)
        layout.addWidget(self.browse_button)

        self.start_time_label = QLabel('Start Time (hh:mm:ss):')
        layout.addWidget(self.start_time_label)

        self.start_time_input = QLineEdit()
        layout.addWidget(self.start_time_input)

        self.stop_time_label = QLabel('Stop Time (hh:mm:ss):')
        layout.addWidget(self.stop_time_label)

        self.stop_time_input = QLineEdit()
        layout.addWidget(self.stop_time_input)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.clicked.connect(self.trim_audio)
        layout.addWidget(self.ok_button)

        self.output_window = QTextEdit()
        self.output_window.setReadOnly(True)
        layout.addWidget(self.output_window)

        self.setLayout(layout)
        self.show()

    def browse(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Audio File', '', 'Audio Files (*.mp3 *.wav *.ogg *.flac);;All Files (*)', options=options)
        if file_name:
            self.file_input.setText(file_name)

    def trim_audio(self):
        file_name = self.file_input.text()
        start_time = self.start_time_input.text()
        stop_time = self.stop_time_input.text()

        if not file_name.lower().endswith(('.mp3', '.wav', '.ogg', '.flac')):
            self.output_window.append('Not an audio file. Please select a valid audio file.')
            return

        try:
            start_time_seconds = sum(int(t) * 60 ** i for i, t in enumerate(reversed(start_time.split(':'))))
            stop_time_seconds = sum(int(t) * 60 ** i for i, t in enumerate(reversed(stop_time.split(':'))))
        except ValueError:
            self.output_window.append('Invalid time format. Please enter time in hh:mm:ss format.')
            return

        if start_time_seconds >= stop_time_seconds:
            self.output_window.append('Start time should be less than stop time.')
            return

        try:
            audio = AudioSegment.from_file(file_name)
            trimmed_audio = audio[start_time_seconds * 1000:stop_time_seconds * 1000]
            output_file_name = f"{os.path.splitext(file_name)[0]}_{convert_seconds_to_hhmmss(start_time_seconds)}_{convert_seconds_to_hhmmss(stop_time_seconds)}.{os.path.splitext(file_name)[1][1:]}"
            trimmed_audio.export(output_file_name, format=os.path.splitext(file_name)[1][1:])
            self.output_window.append('Success')
        except Exception as e:
            self.output_window.append(f'Error: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_selector = FileSelector()
    sys.exit(app.exec_())
