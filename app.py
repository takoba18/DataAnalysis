import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.write("""
# Social media usage

""")
st.sidebar.header("What would you like to display")
option = st.sidebar.selectbox(
    ' Choose ',
    ('Mobile', 'Web', 'Male', 'Female', 'Gender', 'Education', 'Political Views', 'Race', 'Religion',
     'Sexual orientation', 'PC or Mac')
)
data = pd.read_csv('WhatsgoodlyData-10.csv')
chart_bi = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Sexual orientation? Bi")].groupby(
        "Answer")["Count"].sum()
chart_gay = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Sexual orientation? Gay")].groupby(
        "Answer")["Count"].sum()
chart_confused = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "Sexual orientation? Confused")].groupby(
        "Answer")["Count"].sum()
chart_straight = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "Sexual orientation? Straight")].groupby(
        "Answer")["Count"].sum()
chart_christian = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Are you? Christian")].groupby(
        "Answer")[
        "Count"].sum()
chart_muslim = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Are you? Muslim")].groupby("Answer")[
        "Count"].sum()
chart_jewish = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Are you? Jewish")].groupby("Answer")[
        "Count"].sum()
chart_none = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Are you? None/Other")].groupby(
        "Answer")[
        "Count"].sum()
chart_white = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "closely identify as? White")].groupby(
        "Answer")["Count"].sum()
chart_black = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "closely identify as? Black")].groupby(
        "Answer")["Count"].sum()
chart_otherRace = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "closely identify as? Other")].groupby(
        "Answer")["Count"].sum()
chart_native = data.loc[(data["Segment Type"] == "Custom") & (
        data["Segment Description"] == "closely identify as? Native American")].groupby("Answer")["Count"].sum()
chart_asian = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "closely identify as? Asian")].groupby(
        "Answer")["Count"].sum()
chart_hispanic = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "closely identify as? Hispanic")].groupby(
        "Answer")["Count"].sum()
chart_liberal = \
    data.loc[
        (data["Segment Type"] == "Custom") & (data["Segment Description"] == "What's your leaning? Liberal")].groupby(
        "Answer")["Count"].sum()
chart_conservative = data.loc[
    (data["Segment Type"] == "Custom") & (data["Segment Description"] == "What's your leaning? Conservative")].groupby(
    "Answer")["Count"].sum()
chart_middle = data.loc[
    (data["Segment Type"] == "Custom") & (data["Segment Description"] == "What's your leaning? In-between")].groupby(
    "Answer")["Count"].sum()
chart_college = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "I'm in? College")].groupby("Answer")[
        "Count"].sum()
chart_otherEdu = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "I'm in? Other")].groupby("Answer")[
        "Count"].sum()
chart_postGrad = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "I'm in? Post-grad")].groupby(
        "Answer")[
        "Count"].sum()
chart_grad = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "I'm in? Grad School")].groupby(
        "Answer")[
        "Count"].sum()
chart_school = \
    data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "I'm in? High School")].groupby(
        "Answer")[
        "Count"].sum()
chart_female = \
    data.loc[(data["Segment Type"] == "Gender") & (data["Segment Description"] == "Female respondents")].groupby(
        "Answer")[
        "Count"].sum()
chart_mobile = data.loc[data["Segment Type"] == "Mobile"].groupby("Answer")["Count"].sum()
chart_web = data.loc[data["Segment Type"] == "Web"].groupby("Answer")["Count"].sum()
chart_male = \
    data.loc[(data["Segment Type"] == "Gender") & (data["Segment Description"] == "Male respondents")].groupby(
        "Answer")["Count"].sum()
chart_mac = \
data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Mac or PC? Mac")].groupby("Answer")[
    "Count"].sum()
chart_pc = \
data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Mac or PC? PC")].groupby("Answer")[
    "Count"].sum()
chart_oth = \
data.loc[(data["Segment Type"] == "Custom") & (data["Segment Description"] == "Mac or PC? Other")].groupby("Answer")[
    "Count"].sum()

if option == "PC or Mac":
    df = pd.DataFrame({"MAC": chart_mac.values,
                       "PC": chart_pc.values,
                       "Other": chart_oth.values},
                      index=chart_mac.index)
    df.plot(kind="bar")
    st.bar_chart(df)

if option == "Sexual orientation":
    df = pd.DataFrame({"Straight": chart_straight.values,
                       "Bi": chart_bi.values,
                       "Confused": chart_confused.values,
                       "Gay": chart_gay.values},
                      index=chart_straight.index)
    df.plot(kind="bar")
    st.bar_chart(df)

if option == "Religion":
    df = pd.DataFrame({"Christian": chart_christian.values,
                       "Muslim": chart_muslim.values,
                       "Other/None": chart_none.values,
                       "Jewish": chart_jewish.values},
                      index=chart_christian.index)
    df.plot(kind="bar")
    st.bar_chart(df)
if option == "Race":
    df = pd.DataFrame({"White": chart_white.values,
                       "Black": chart_black.values,
                       "Other": chart_otherRace.values,
                       "Native America": chart_native.values,
                       "Asian": chart_asian.values,
                       "Hispanic": chart_hispanic.values},
                      index=chart_white.index)
    df.plot(kind="bar")
    st.bar_chart(df)
if option == "Political Views":
    df = pd.DataFrame({"Liberal": chart_liberal.values,
                       "Conservative": chart_conservative.values,
                       "In-Between": chart_middle.values},
                      index=chart_liberal.index)
    df.plot(kind="bar")
    st.bar_chart(df)
if option == "Education":
    df = pd.DataFrame({"Grad School": chart_grad.values,
                       "High School": chart_school.values,
                       "College": chart_college.values,
                       "Other": chart_otherEdu.values,
                       "Post-Grad": chart_postGrad.values},
                      index=chart_grad.index)
    df.plot(kind="bar")
    st.bar_chart(df)
if option == "Gender":
    df = pd.DataFrame({"Male": chart_male.values,
                       "Female": chart_female.values},
                      index=chart_female.index)
    df.plot(kind="bar")
    st.bar_chart(df)
if option == "Female":
    labels = chart_female.index
    sizes = chart_female.values
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
if option == "Mobile":
    labels = chart_mobile.index
    sizes = chart_mobile.values
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
if option == "Web":
    labels = chart_web.index
    sizes = chart_web.values
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
if option == "Male":
    labels = chart_male.index
    sizes = chart_male.values
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
