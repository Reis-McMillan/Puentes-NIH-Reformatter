from tkinter import filedialog

import pandas as pd
from tkinter import *

WAVE = 'W1'
PARTICIPANT_TYPE = 'C'


def find_Abnormalitites(input_path: str):
    df = pd.read_csv(input_path)

    null_indicies = df[df['PIN'].isnull()].index
    df.drop(null_indicies, inplace=True)

    counts = df['PIN'].value_counts()
    abnormalities = counts[counts > 3].index.tolist()

    if 'PIN' in abnormalities:
        abnormalities.remove('PIN')

    return abnormalities


def to_Final_CSV(input_path: str):
    df = pd.read_csv(input_path)

    df['Inst'].head()

    null_indices = df[df['PIN'].isnull()].index
    df.drop(null_indices, inplace=True)
    label_indices = df[df['PIN'] == 'PIN'].index
    df.drop(label_indices, inplace=True)

    df.reset_index(inplace=True, drop=True)

    sortedDf_Dimensional = df[df['Inst'].str.contains('Dimensional')][['PIN',
                                                                       'RawScore',
                                                                       'Computed Score',
                                                                       'Uncorrected Standard Score',
                                                                       'Age-Corrected Standard Score',
                                                                       'National Percentile (age adjusted)',
                                                                       'Fully-Corrected T-score']]

    sortedDf_Dimensional.rename(columns={'RawScore': 'Dimensional Card Sort RawScore',
                                         'Computed Score': 'Dimensional Card Sort Computed Score',
                                         'Uncorrected Standard Score': 'Dimensional Card Sort Uncorrected Standard Score',
                                         'Age-Corrected Standard Score': 'Dimensional Card Sort Age-Corrected Standard Score',
                                         'National Percentile (age adjusted)': 'Dimensional Card Sort National Percentile (age adjusted)',
                                         'Fully-Corrected T-score': 'Dimensional Card Sort Fully-Corrected T-score'},
                                inplace=True)

    sortedDf_Flanker = df[df['Inst'].str.contains('Flanker')][['PIN',
                                                               'RawScore',
                                                               'Computed Score',
                                                               'Uncorrected Standard Score',
                                                               'Age-Corrected Standard Score',
                                                               'National Percentile (age adjusted)',
                                                               'Fully-Corrected T-score']]

    sortedDf_Flanker.rename(columns={'RawScore': 'Flanker Inhibitory Control and Attention RawScore',
                                     'Computed Score': 'Flanker Inhibitory Control and Attention Computed Score',
                                     'Uncorrected Standard Score': 'Flanker Inhibitory Control and Attention Uncorrected Standard Score',
                                     'Age-Corrected Standard Score': 'Flanker Inhibitory Control and Attention Age-Corrected Standard Score',
                                     'National Percentile (age adjusted)': 'Flanker Inhibitory Control and Attention National Percentile (age adjusted)',
                                     'Fully-Corrected T-score': 'Flanker Inhibitory Control and Attention Fully-Corrected T-score'},
                            inplace=True)

    sortedDf_Picvocab = df[df['Inst'].str.contains('Picture')][['PIN',
                                                                'Theta',
                                                                'SE',
                                                                'Uncorrected Standard Score',
                                                                'Age-Corrected Standard Score',
                                                                'National Percentile (age adjusted)',
                                                                'Fully-Corrected T-score']]

    sortedDf_Picvocab.rename(columns={'Theta': 'Picture Vocabulary Theta',
                                      'SE': 'Picture Vocabulary SE',
                                      'Uncorrected Standard Score': 'Picture Vocabulary Uncorrected Standard Score',
                                      'Age-Corrected Standard Score': 'Picture Vocabulary Age-Corrected Standard Score',
                                      'National Percentile (age adjusted)': 'Picture Vocabulary National Percentile (age adjusted)',
                                      'Fully-Corrected T-score': 'Picture Vocabulary Fully-Corrected T-score'},
                             inplace=True)

    sortedDf = pd.merge(sortedDf_Dimensional, sortedDf_Flanker, how='outer', on=['PIN'])
    sortedDf = sortedDf.merge(sortedDf_Picvocab, how='outer', on=['PIN'])

    sortedDf.insert(1, 'Wave', 1)
    sortedDf.insert(2, 'Participant', PARTICIPANT_TYPE)

    lang_indices = df['PIN'].drop_duplicates().index
    language = df.iloc[lang_indices][['PIN', 'Language']]
    sortedDf = sortedDf.merge(language, how='outer', on=['PIN'])
    language = sortedDf.pop('Language')
    sortedDf.insert(3, 'Language', language)

    sortedDf['PIN'] = sortedDf['PIN'].astype(str)
    sortedDf['PIN'] = sortedDf['PIN'].apply(str.upper)
    sortedDf['PIN'] = sortedDf['PIN'].str.replace(WAVE, '')
    sortedDf['PIN'] = sortedDf['PIN'].str.replace('[^0-9]', '', regex=True)
    empty_indicies = sortedDf[sortedDf['PIN'] == ''].index
    sortedDf.drop(empty_indicies, inplace=True)

    sortedDf['PIN'] = sortedDf['PIN'].astype(int)
    sortedDf.drop_duplicates(inplace=True)
    sortedDf.sort_values(by='PIN', inplace=True)

    output_path = filedialog.asksaveasfile(title='Save File As',
                                           initialfile='.csv',
                                           filetypes=(('csv files', '*.csv*'), ('all files', '*.*')))

    sortedDf.to_csv(output_path, index=False, lineterminator='\n')


def on_wave_select(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    WAVE = w.get(index)


def on_participant_select(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    PARTICIPANT_TYPE = w.get(index)


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("csv files", "*.csv*"), ('all files', '*.*')))
    return filename


def prelim_check():
    filename = browse_files()
    abnormalities = find_Abnormalitites(filename)

    output_text.set(f'There appears to be some abnormalities in rows: {abnormalities}. Please check '
                    f'these rows before reformatting the data.')


def reformat():
    filename = browse_files()
    to_Final_CSV(filename)

    output_text.set('The file has successfully been reformatted.')


if __name__ == '__main__':
    window = Tk()
    window.geometry('500x500')
    window.title('Puentes NIH Data Reformatter')

    wave_frame = Frame(window)
    wave_label = Label(wave_frame, text='Wave')
    wave_label.pack()
    wave_listbox = Listbox(wave_frame,
                           selectmode=SINGLE,
                           activestyle='dotbox',
                           height=3,
                           exportselection=False)
    wave_listbox.insert(1, 'W1')
    wave_listbox.insert(2, 'W2')
    wave_listbox.insert(3, 'W3')
    wave_listbox.bind('<<ListboxSelect>>', on_wave_select)
    wave_listbox.pack()

    participant_frame = Frame(window)
    participant_label = Label(wave_frame, text='Participant Type')
    participant_label.pack()
    participant_listbox = Listbox(wave_frame,
                                  selectmode=SINGLE,
                                  activestyle='dotbox',
                                  height=2,
                                  exportselection=False)
    participant_listbox.insert(1, 'C')
    participant_listbox.insert(2, 'P')
    participant_listbox.bind('<<ListboxSelect>>', on_participant_select)
    participant_listbox.pack()

    button_frame = Frame(window)
    button_prelim = Button(button_frame,
                           text="Preliminary Check",
                           command=prelim_check)
    button_prelim.pack()
    button_reformat = Button(button_frame,
                             text='Reformat NIH Data',
                             command=reformat)
    button_reformat.pack()

    text_frame = Frame(window)
    output_text = StringVar(value='')
    text_lb = Label(text_frame,
                    textvariable=output_text,
                    justify=LEFT,
                    wraplength=350)
    text_lb.pack(side=TOP)

    button_frame.grid(row=1, column=0)
    wave_frame.grid(row=0, column=0)
    text_frame.grid(row=0, column=1, columnspan=2)
    window.mainloop()
