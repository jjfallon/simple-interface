from sklearn.datasets import fetch_20newsgroups
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact


# Get some test text data
text_data = fetch_20newsgroups(subset='train', remove=['headers', 'footers', 'quotes'] ).data


def view_text(index):
    '''View the text at the given index '''

    print text_data[index]


def view_wordcloud(index):
    '''Plot a wordcloud of the text at a given index '''

    wc = WordCloud(random_state=42).generate( text_data[index] )
    plt.figure(figsize=(12,10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def classify(index):
    '''Classify document at the given index'''
    print "Catagory 1"


def select_function(option, index):
    ''' Select what function to run on document at given index'''

    if option == "View text":   
        view_text(index)
    elif option == "Show word cloud":
        view_wordcloud(index)
    elif option == "Classify":
        classify(index)
    else:
	print ""


def choose_what_to_do():
    ''' Pick a document and choose what to do'''
    
    # Define document ID selecter widget
    w_doc = widgets.BoundedIntText(
        min=0,
        max=11313,
        step=1,
        description='Document ID:',
        disabled=False
    )

    # Define activity chooser widget
    w_radio = widgets.RadioButtons(
        options=['Nothing', 'View text', 'Show word cloud', 'Classify'],
        description='  ',
        disabled=False, 
    )

    interact(select_function, index=w_doc, option=w_radio)


