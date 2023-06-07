# import streamlit as st

# #title - used to add the title of an app
# st.title("Muwahahhahaha! Here my shitty test")

# #header
# st.header("Mmm.. A cAlcUlAtOr? ..")

# # #subheader
# # st.subheader("bae jus said tht she hates me T.T ... hee she said it in cute way tho keke")

# # #information 
# # st.info("SO yeah THIS IS MY SHIT down there")

# # #warning
# # st.warning("U r going to Die in 3mins . . ....")

# # #write
# # st.write("write a name tht u wanna kill here. .. .. .x")

# n1 = st.number_input('Number a:')
# st.title("+")
# n2 = st.number_input('Number b:')
# st.title("=")

# result = n1+n2

# st.write('the combination of ',n1,' and ',n2,' is ',result)

import streamlit as st
st.title('BMI Calculator')

weight=st.number_input("Enter your weight (in kgs)")
height=st.number_input("Enter your height (in cms)")


if(st.button('Calculate BMI')):

    if (weight==0 or height==0):
        st.text("Enter some value of height and weight")
    else:
        st.text("Your BMI Index is {}.".format(bmi))

        if(bmi<16):
            st.error("You are Extremely Underweight")
        elif(bmi>=16 and bmi<18.5):
            st.warning("You are Underweight")
        elif(bmi>=18.5 and bmi<25):
            st.success("Healthy")
        elif(bmi>=25 and bmi<30):
            st.warning("You are Overweight")
        elif(bmi>=30):
            st.error("You are Extremely Overweight")




