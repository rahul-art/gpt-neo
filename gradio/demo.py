from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')
import gradio as gr
def outbreak_forecast(How_Old,Gender, Scheduler_Name,Patient_name, First_time,Adult_Child_or_Multiple_Family_Members,
            Virtual_or_In_person_Appointment,Who_For,Appointment_Date,Appointment_Time,This_week_or_next,Location,
            Lower_Price_or_Flexible_Payment,Sleep_Apnea,Migraines):
  if Sleep_Apnea=="No" and Migraines=="No":
    disease = "he/She doesn't have any sleep apnea or migraines."
  elif Sleep_Apnea=="Yes" and Migraines=="Yes":
    disease = "he/She has both sleep apnea and migraines."
  elif Sleep_Apnea=="Yes" and Migraines=="No":
    disease = "he/She has only sleep apnea and not migraines."
  elif Sleep_Apnea=="No" and Migraines=="Yes":
    disease = "he/She has only Migraines and not Sleep_Apnea."
  prompt=f"""Human: write an email reponse for Mom (Mary) she was looking for an new patient appt for her son Jimmy, who was 10 yrs old, and hey had been to a previous consult and didn't accept treatment because the other practice quoted them a month payment that was to high for their budget.\nAI: Hi, Mary! \n\nThank you for taking the time to contact SmileMaker Orthodontics. I am pleased to hear that you are considering treatment for your daughter, Lydia.\n\nWe are excited to provide you with a complimentary new patient evaluation for next Tuesday morning, as you requested.  I made a special slot for you and Lydia at 8:30am! You’ll only need to set aside 60 minutes for your appointment.\n\nSmileMaker Orthodontics is a premier orthodontic practice in the area. We are a full service orthodontic practice that offers comprehensive treatment options, specializing in children. We are committed to providing the highest quality orthodontic care and show stopping results!\n\nI saw you said you'd want a lower start-up cost and more flexible payment choices. I'm happy to say that we have a variety of payment options for you to choose, and we won't allow budget get in the way of her achieving the beautiful smile she deserves.\n\nPlease call, email or text us if you have any questions at all, and we look forward to seeing you and Lydia then!\n\nThank you,\n\nDoctor’s Name\n---------------\nDear Mary:\n\nThank you for reaching out to us regarding Lydia. It is our pleasure to work with families like yours, and we look forward to meeting you!\n\nLydia's orthodontic treatment plan will include everything she needs to achieve the perfect smile she deserves!\n\nI saw you requested a reduced start-up cost and payment flexibility. We offer several affordable payment plans, and we won't let her budget prevent her from getting the gorgeous smile she deserves.\n\nYou had requested an appointment for Tuesday morning the following week, and we worked to open up a slot for 9:00am.\n\nThank you,\n-----------\nHi Mary,\n\nThank you for taking the time to inquire about orthodontic treatment for Lydia. I am happy to share information about our practice and the options we provide.\n\nDr. Burton is a highly respected orthodontist, who is known for his state-of-the-art treatment methods and results. \n\nOur affordable orthodontic treatment plans are perfect for families with that prefer reduced start up cost with flexible payments, such as yours. \n\nWe offer flexible payment plans designed to fit your ideal budget. I'm looking forward to sharing our easy budget options with you, and finding a solution that is affordable and convenient for you.\n\nI have you scheduled for next Tuesday morning as you requested, and I made a slot for you at 10:00 am!\n\nWe look forward to seeing you and Lydia then!\n\nThank you,\n\nDoctor’s Name\n-----------\nHi, Mary! \n\nI want to thank you for contacting SmileMaker Orthodontics to schedule an appointment for Lydia. I am glad that you are considering us for your daughter’s orthodontic treatment. \n\nI saw that you mentioned that you would prefer reduced start up cost with flexible payment options.  I am happy to say that we offer several payment options that you can consider, and we won’t let budget stand in the way of Lydia getting the remarkable smile she deserves.\n\nYou had asked for an appointment Tuesday morning, next week.\n\nWe worked on our schedule and found a way to fit you in right at 9:00am!\n\nI have you scheduled for that time slot, so let me know right away if we need to try and move that earlier or later and if not, Dr. Burton and the team are excited to meet you then!\n\nPlease give us a call or email with any questions at all!\nHuman: Write an email for Rahul danu, this is his First time here he is an Adult. he wants an In person Appointment for himself on Friday evening for London location, he prefers Lower Price. he doesn't have migraine and Sleep Apnea.\nAI: Dear Rahul,\n\nThank you for your interest in SmileMaker Orthodontics. We would be happy to accommodate your request for a Friday evening appointment for In-person service.\n\nWe offer a variety of payment plans to fit your needs. We also offer a lower starting cost than most of our competitors.\n\nThe location for this appointment is in London and the time is at 8:00pm.\n\nI hope you have a wonderful day.\n\nThank you,\n\nSmileMaker Orthodontics\nHuman: Write an email for {Scheduler_Name}, this is his/her {First_time} here, he/she is an {Adult_Child_or_Multiple_Family_Members}. he/She wants an {Virtual_or_In_person_Appointment} for {Who_For} on {Appointment_Date} {Appointment_Time} for {Location} location, he/she prefers {Lower_Price_or_Flexible_Payment}. {disease}\nAI:""".format(Scheduler_Name,First_time,Adult_Child_or_Multiple_Family_Members,Virtual_or_In_person_Appointment,Who_For,Appointment_Date,Appointment_Time,Location,Lower_Price_or_Flexible_Payment,disease),
  response=generator(prompt,do_sample=True,temperature=0.7, min_length=1200,max_length=1210)[0]['generated_text']
  return response.replace(''.join(prompt),'').split("\nHuman:")[0].split("\nAI:")[0]

How_Old = gr.inputs.Slider(1, 60)
Gender = gr.inputs.CheckboxGroup(["Male", "Female","other"])
Scheduler_Name = gr.inputs.Textbox()
Patient_name=gr.inputs.Textbox()
First_time = gr.inputs.Textbox()
Adult_Child_or_Multiple_Family_Members = gr.inputs.Textbox()
Virtual_or_In_person_Appointment = gr.inputs.Textbox()
Who_For = gr.inputs.Textbox()
Appointment_Date = gr.inputs.Radio(["Mon", "Tue", "Wed", "Thr",'Fri',"Sat","sun"])
Appointment_Time = gr.inputs.CheckboxGroup(["Morning", "afternoon","evening"])
This_week_or_next = gr.inputs.Radio(["this week", "next week"])
Location = gr.inputs.Textbox()
Lower_Price_or_Flexible_Payment = gr.inputs.Textbox()
Sleep_Apnea = gr.inputs.Dropdown(["Yes", "No"])
Migraines = gr.inputs.Dropdown(["Yes", "No"])

iface = gr.Interface(fn=outbreak_forecast,
    inputs=[How_Old,Gender, Scheduler_Name,Patient_name, First_time,Adult_Child_or_Multiple_Family_Members,
            Virtual_or_In_person_Appointment,Who_For,Appointment_Date,Appointment_Time,This_week_or_next,Location,
            Lower_Price_or_Flexible_Payment,Sleep_Apnea,Migraines], outputs="textbox")
iface.test_launch()
if __name__ == "__main__":
    iface.launch()
