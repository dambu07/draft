import streamlit as st
import openai
import os

api_key = os.environ.get("OPENAI_API_KEY")
# Set your OpenAI API key
openai.api_key = api_key


class Law:
    def custom(user_name, user_address, user_contact_details, document_date, specific_details,
               governing_jurisdiction, witness_name, witness_address, notary_details, legal_references,
               specific_language, witness_signatures):
        # Generate a response using GPT-3
        response = openai.ChatCompletion.create(
            engine="text-davinci-003",
            prompt="You are a Legal Document Drafting Bot. Please draft a legal document based on the following information:\n"
                   f"Name: {user_name}\n"
                   f"Address: {user_address}\n"
                   f"Contact Details: {user_contact_details}\n"
                   f"Document Date: {document_date}\n"
                   f"What the document is about: {specific_details}\n"
                   f"Jurisdiction: {governing_jurisdiction}\n"
                   f"Witness Name: {witness_name}\n"
                   f"Witness Address: {witness_address}\n"
                   f"Notary Details: {notary_details}\n"
                   f"Legal References: {legal_references}\n"
                   f"Language: {specific_language}\n"
                   f"Witness Signatures (yes or no): {witness_signatures}\n"
                   "IMPORTANT!: IF THE VALUE IS N/A THEN SKIP THAT FIELD!",
            max_tokens=1000
        )

        return response.choices[0].text.strip()

    def termination(organization, organ_address, state, name, title, department, first_date, last_date, when, reason,
                    relevant_names,
                    severance, amount, return_property, nda, transition, language_tone, additional_info, hr, contact):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="You are a termination email writing bot. Use the following information to draft a termination "
                   "letter:\n"
                   f"Organization Name: {organization}\n"
                   f"Organization Address: {organ_address}\n"
                   f"Employee State/City/Country: {state}\n"
                   f"Employee Name: {name}\n"
                   f"Job Title: {title}\n"
                   f"Department of Work: {department}\n"
                   f"Date of Hire: {first_date}\n"
                   f"Last working Day: {last_date}\n"
                   f"Whether the termination is immediate or with notice: {when}\n"
                   f"Reason for Termination: {reason}\n"
                   f"Name(s) and Title(s) of the people present during the termination meeting: {relevant_names}\n"
                   f"Any severance: {severance}\n"
                   f"Benefits and/or Severance: {amount}"
                   f"Property to Return: {return_property}\n"
                   f"Any NDA: {nda}\n"
                   f"Next steps and Transition: {transition}\n"
                   f"Language and tone: {language_tone}\n"
                   f"Any extra info: {additional_info}\n"
                   f"HR Rep will be contacting them: {hr}\n"
                   f"Contact Details: {contact}\n"
                   f"SIGN THE LETTER OFF WITH THE ORGANIZATION'S NAME"
                   f"DRAW UP A TERMINATION EMAIL USING THIS INFORMATION",
            max_tokens=1000
        )

        return response.choices[0].text.strip()

    def cease(name, legal_name, rec_name, details, basis, evidence, demand, consequences,
              contact, extra, tone):
        response = openai.Completion.create(engine="text-davinci-003",
                                            prompt="You are a cease and desist writing bot. Use the following information to draft a cease and desist document:\n"
                                                   f"Sender Name: {name}\n"
                                                   f"Legal representative's name or law firm: {legal_name}\n"
                                                   f"Recipient Information: {rec_name}\n"
                                                   f"Description of infringement: {details}\n"
                                                   f"Legal Basis: {basis}\n"
                                                   f"Leave Area for evidence if there is any: {evidence}\n"
                                                   f"Demand: {demand}\n"
                                                   f"Consequences of Non-Compliance: {consequences}\n"
                                                   f"Contact Information for Response: {contact}\n"
                                                   f"Specific Wants: {extra}\n"
                                                   f"Language and/or Tone: {tone}",
                                            max_tokens=1000)
        return response.choices[0].text.strip()


def main():
    st.set_page_config(
        page_title="Legal Document Drafting Chatbot",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="logo.png",  # Set the icon for the page
    )

    # Custom CSS to change the theme to black and gold
    st.markdown(
        """
        <style>
        body {
            color: black;
            background-color: gold;
        }
        .st-bd {
            background-color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit UI
    st.image("logo.png", width=150)  # Adjust the image width to make it smaller

    st.title("Legal Document Drafting Chatbot")
    st.markdown("Welcome to the Legal Document Drafting Chatbot! Please enter the following information:")

    type = st.selectbox("What type of document do you want to draft?",
                        (" ", "Custom", "Termination", "Cease and Desist"))

    if type == "Custom":
        # Collect user information
        user_name = st.text_input("Full Legal Name:")
        user_address = st.text_area("Address:")
        user_contact_details = st.text_input("Contact Details:")
        document_date = st.text_input("Document's Date:")
        specific_details = st.text_area("Specific Details:")
        governing_jurisdiction = st.text_input("Governing Jurisdiction:")
        witness_required = st.radio("Does the document require witnesses?", ("Yes", "No"))

        if witness_required == "Yes":
            witness_name = st.text_input("Witness's Full Legal Name:")
            witness_address = st.text_area("Witness's Address:")
            witness_signatures = st.radio("Are witnesses present and willing to sign?", ("Yes", "No"))
        else:
            witness_name = "N/A"
            witness_address = "N/A"
            witness_signatures = "N/A"

        notary_details = st.text_area("Notary Public Details:")
        legal_references = st.text_area("Legal References:")
        specific_language = st.text_area("Specific Language or Wording:")

        disclaimer = "IMPORTANT!: If the value is N/A, then skip that field in the document."

        st.markdown(f"<p style='color:red;'>Disclaimer: {disclaimer}</p>", unsafe_allow_html=True)

        st.write("Please ensure you have entered all information accurately.")
        if st.button("Generate Legal Document"):
            # Generate the response from the chatbot
            bot_response = Law.custom(user_name, user_address, user_contact_details, document_date,
                                      specific_details,
                                      governing_jurisdiction, witness_name, witness_address,
                                      notary_details, legal_references,
                                      specific_language, witness_signatures)
            # Display the bot's response to the user
            st.write("Bot's Response:")
            st.info(bot_response)

    elif type == "Termination":
        organization = st.text_input("Name of organization: ")
        organ_address = st.text_input("Organization Address: ")
        state = st.text_input("Employee State/Country/City")
        name = st.text_input("Employee Name: ")
        title = st.text_input("Job Title: ")
        department = st.text_input("Department: ")
        first_date = st.text_input("Date of Hire: ")
        last_date = st.text_input("Last Working Date: ")
        when = st.radio("Is the termination immediate or with notice?", ("Immediate", "With Notice"))
        reason = st.text_area("Reason for Termination: ")
        relevant_names = st.text_area("Name(s) and Title(s) of the people present during the termination meeting:")
        severance = st.radio("Any Severance or Benefits: ", ("Yes", "No"))

        if severance == "Yes":
            amount = st.text_input("Enter Benefits and Severance: ")

        return_property = st.text_input("Property to be Returned: ")
        nda = st.text_area("NDA information if any (skip if none)")
        transition = st.text_area("Next steps, transition and concurrent tasks: ")
        language_tone = st.text_input("Specific Language or Tone: ")
        additional_info = st.text_area("Any Additional Information: ")
        hr = st.text_input("HR Rep: ")
        contact = st.text_input("Contact Details")

        st.write("Please ensure you have entered all information accurately.")

        if st.button("Draft Termination Letter"):
            bot_response = Law.termination(organization, organ_address, state, name, title, department, first_date,
                                           last_date, when, reason, relevant_names,
                                           severance, amount, return_property, nda, transition, language_tone,
                                           additional_info, hr, contact)

            st.write("Bot's Response:")
            st.info(bot_response)

    elif type == "Cease and Desist":
        name = st.text_input("Enter your full legal name: ")
        legal_name = st.text_input("Enter your legal representative or law firm's name: ")
        rec_name = st.text_area("Enter all relevant details related to the recipient: ")
        details = st.text_area("Description of infringement: ")
        basis = st.text_area("Legal Basis: ")
        evidence = st.radio("Do you have any evidence: ", ("Yes", "No"))
        demand = st.text_input("Enter your demands: ")
        consequences = st.text_area("What will be the consequences: ")
        contact = st.text_input("Your contact info for response: ")
        extra = st.text_area("Enter any specific wants that you have such as an apology: ")
        tone = st.text_input("Enter language and/or tone: ")

        st.write("Please ensure you have entered all information accurately.")

        if st.button("Draft Cease and Desist Letter"):
            bot_response = Law.cease(name, legal_name, rec_name, details, basis, evidence, demand, consequences,
                                     contact, extra, tone)
            st.write("Bot's Response:")
            st.info(bot_response)


if __name__ == "__main__":
    main()
