# Création des fichiers avec les réponses
files_with_answers = {
    '0-answer.txt': 'type',
    '1-answer.txt': 'id',
    '2-answer.txt': 'No',
    '3-answer.txt': 'Yes',
    '4-answer.txt': 'Yes', 
    '5-answer.txt': 'No',
    '6-answer.txt': 'True',
    '7-answer.txt': 'True',
    '8-answer.txt': 'True',
    '9-answer.txt': 'True',
    '10-answer.txt': 'True',
    '11-answer.txt': 'False',
    '12-answer.txt': 'True',
    '13-answer.txt': 'True',
    '14-answer.txt': '[1, 2, 3, 4]',
    '15-answer.txt': '[1, 2, 3]',
    '16-answer.txt': '1',
    '17-answer.txt': '[1, 2, 3, 4]',
    '18-answer.txt': '[1, 2, 3]',
    '19-copy_list.py': 'def copy_list(a_list): return a_list.copy()',
    '20-answer.txt': 'Yes',
    '21-answer.txt': 'Yes', 
    '22-answer.txt': 'No',
    '23-answer.txt': 'Yes',
    '24-answer.txt': 'False',
    '25-answer.txt': 'True',
    '26-answer.txt': 'True',
    '27-answer.txt': 'No',
    '28-answer.txt': 'Yes',
}

# Écriture dans chaque fichier
for filename, answer in files_with_answers.items():
    with open(filename, 'w') as f:
        f.write(answer)