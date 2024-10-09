import streamlit as st
import pandas as pd

def grade_attendance(participation:float)->str:
    if participation == 0.0:
        return "AB"
    if participation < 0.5:
        return "np"
    return"+"

st.title('Xavier polling report')
#EXTRACTION
#EXTRACT ROSTER
roster = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv")

#EXTRACT EACH POLL
polls=[]
dates = ["2024-01-08", "2024-01-15","2024-01-22","2024-01-29"]
for date in dates:
    poll = f"https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/poll-responses-{date}.csv"
    poll_df = pd.read_csv(poll)
    #add lineage
    poll_df['date'] = date
    #add poll to list
    polls.append(poll_df)


#Combine all polls together
polls_df = pd.concat(polls,ignore_index=True)  

#TRANSFORMATION
combined_df = pd.merge(polls_df,roster,how='right',left_on='student_id',right_on='netid') 

#poll counts by each date
poll_counts = combined_df.pivot_table(index='date',values='poll_num',aggfunc='max')

#count of student responses by date
student_responses = combined_df.pivot_table(index='netid',columns='date',values='answer',aggfunc='count')
student_responses = student_responses.fillna(0)

#change poll responses to percentages
for col in student_responses.columns:
    student_responses[col] = student_responses[col]/poll_counts.loc[col,'poll_num']
#convert percentages to grades
for col in student_responses.columns:
    student_responses[col] = student_responses[col].apply(grade_attendance)

#total class sessions, total absences, total no participation, total plus, pct of sessions absent or no participation
summary = student_responses.copy()
summary['sessions'] = len(summary.columns)
summary['ab'] = summary.apply(lambda row: row.str.count('AB').sum(),axis=1) 
summary['np'] = summary.apply(lambda row: row.str.count('np').sum(),axis=1)
summary['pct'] = (summary['ab']+summary['np'])/summary['sessions']
#add names on netid
summary = pd.merge(roster,summary,left_on='netid', right_index=True)
#DISPLAY
st.dataframe(summary)
#DOWNLOAD
st.download_button('Download Report',data=summary.to_csv(),file_name='polling_report.csv',mime='text/csv')