# simple-interface

A mock up of using `jupyter` notebooks to create a very simple interface to a mode for non-techical customers to use. This uses `ipywidgets` to provide the interactivty and you need to run the following command:

```bash
jupyter nbextension enable --py widgetsnbextension
```
to enable you to use these widgets.

It is not straightforward in `jupyter` to hide the code cells, so here all the code has been put into a file called `model_api.py`. This includes simple wrappers to commands you want the user to run. This files requires the packages `scikit-learn`, `wordcloud`, `matplotlib`, and `ipywidgets` to be installed.

In this toy example text data from the 20 Newsgroups is retreived. You then specify which document you are interested in (the document IDs run from 0 to 11,313) and then you specify what you want to do with that document. You can view the text, show a word cloud, or pass it through a classifier (though here the classifier always returns one).

In order to simplify this example the model is coded into the module, and the data loader is also within there. In practice you would probably want to pickle a pre-trained model and point the notebook at some saved data.

