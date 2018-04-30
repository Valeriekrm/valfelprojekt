from __future__ import print_function, division
import nltk
import sys, os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify
import pickle
import smtplib
import time
import imaplib
import email
import base64


stoplist = stopwords.words('english') #stopwords sind Füllwörter wie der die das the and und...

stoplist = stopwords.words('german')

    # Aufruf des Ordners und Sammeln der darin beinhalteten Dateien

def init_lists(Ordner):
    
    a_Liste = []
    #Ordner welcher übergeben wurde wird ausgelesen
    Dateienliste = os.listdir(Ordner)
    for a_Datei in Dateienliste:
        f = open(Ordner + a_Datei, 'r', encoding="utf-8", errors='ignore')
        #wird in a Liste gepackt und gelesen, dann geschlossen
        a_Liste.append(f.read())
    f.close()
    return a_Liste

def vorprozess(satz):
    lemmatizer = WordNetLemmatizer()
    #gibt die kleingeschriebenen wörter zurück
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(satz)]



def get_features(text, setting):
    # bag-of-words model (BoW model) can be applied to image classification, by treating image features as words
    if setting=='bow':
        # wort wird gezählt und vorprozess (lemmatizer) übergeben wenn kein stopwort
        return {word: count for word, count in Counter(vorprozess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in vorprozess(text) if not word in stoplist}

def train(features, samples_proportion):

    #trainingsgröße = Alle Eigenschaften * Stichprobenanteil
    train_size = int(len(features) * samples_proportion)
    
    # Initialisieren des Training und Testsets
    #trainingsset bis zur trainingsgröße und testset ab diesem bis zum ende - Grund: die Set Größe ändert sich immer wieder, kann aber auch beloebig angepasst werden
    trainingset, testset = features[:train_size], features[train_size:]
    print ('Trainingset Größe = ' + str(len(trainingset)) + ' emails')
    print ('Testset Größe = ' + str(len(testset)) + ' emails')
    
    # Trainieren des Classifiers
    # Eigenschaften werden übergeben
    classifier = nltk.NaiveBayesClassifier.train(trainingset)
    return trainingset, testset, classifier

def leistung(trainingset, testset, classifier):
    # Richtigkeit des Classifiers auf dem Training und Testsets testen
    print ('Accuracy on the training set = ' + str(nltk.classify.accuracy(classifier, trainingset)))
    print ('Accuracy of the test set = ' + str(nltk.classify.accuracy(classifier, testset)))

    
    # Die ersten 20 wichtigsten Wörter für den Classifier testen
    classifier.show_most_informative_features(46)

def read_email_from_gmail():
    try:
        
        ORG_EMAIL   = "@gmail.com"
        FROM_EMAIL  = "valeriefelixprojekt" + ORG_EMAIL
        FROM_PWD    = decode('deinemutter', 'w5rDhsOVw5PDl8OWw5rCpsKkwoY=')
        SMTP_SERVER = "imap.gmail.com"
        SMTP_PORT   = 993
        
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        
        for i in reversed(id_list):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
            print('From : ' + email_from + '\n')
            print('Subject : ' + email_subject + '\n')
            
            kleister = get_features (email_subject, '')
            
            print (kleister)
            print (str(classifier.classify (kleister)))
        pw = 0
        FROM_PWD = 0
    except Exception as e:
            print(str(e))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

    # Initialisieren 

spam = init_lists('/code/MeineSpam/')
ham = init_lists('/code/MeineHam/')

allemails = [(email, 'spam') for email in spam]
allemails += [(email, 'ham') for email in ham]
random.shuffle(allemails)
    #Anzahl aller Mails wird ausgegeben
print ('Corpus size = ' + str(len(allemails)) + ' emails')

    # Ausgabe der wichtigsten Wörter
    # holt zuerst WÖrter aus der Email raus, übergibt sie an den Lemmatizer und zählt diese
alleEigenschaften = [(get_features(email, ''), label) for (email, label) in allemails]

    #gibt die gesammelten Wörter zuvor aus
print ('Collected ' + str(len(alleEigenschaften)) + ' feature sets')

    # Aufruf des Trainings des Classifiers
    #alle Eigenschaften werden an train übergeben und einen Stichprobenanteil von 80%
trainingset, testset, classifier = train(alleEigenschaften, 0.8)

    # Aufruf der Leistungsbewertung
leistung(trainingset, testset, classifier)

f = open('/code/klasse.txt', 'wb')
pickle.dump(classifier, f)
f.close()


#nutzen des classifiers ohne die einspeisung

f = open('/code/klasse.txt', 'rb')
classifier = pickle.load(f)
f.close()

read_email_from_gmail()

