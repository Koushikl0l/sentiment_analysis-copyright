import streamlit as st
import load_pred as model


def about():
	st.write(
		'''
		**Haar Cascade** is an object detection algorithm.
		It can be used to detect objects in images or videos. 

		The algorithm has four stages:

			1. Haar Feature Selection 
			2. Creating  Integral Images
			3. Adaboost Training
			4. Cascading Classifiers



View Dev-k web :point_right: http://dev-k-copyright.herokuapp.com/
		''')
activities = ["Home", "About"]
choice = st.sidebar.selectbox("Pick something fun", activities)
def main():
    if choice=="Home":
        st.title("Sentiment Analysis --text classification ")
        st.write("**Model:Here we used BERT as a pre-trained model**")
        text_inp = st.text_area("Enter sentence for sentiment")
        st.sidebar.info('© 2021 Copyright: Dev-k')   

        if st.button("Process") and text_inp:
            pred=model.predict(text_inp)
            res=''
            if pred[0][0]>.5:
                        res='positive'
            else:
                res='Negative'
        
            st.success("Sentiment: {} ".format(res))
    elif choice == "About":
    	about()

if __name__ == "__main__":
    main()
