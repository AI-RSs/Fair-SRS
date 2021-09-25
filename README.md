# Fair-SRS

This is a demonstrates for **Fair-SRS**, a Fair Session-based Recommendation System that predicts user’s next click based on their historical and current session sequences of click behaviour.
Fair-SRS provides personalized and diversified recommendations in two main steps: 

     1. forming user's session graph embeddings based on their long- and short-term interests, and
     
     2. computing the user's level of interest in diversity based on their recently-clicked items' similarity.

In real-world scenarios, **users** tend to interact with more or less contents in different times and **providers** expect to receive more exposure for their items. 

To achieve the objectives of both sides, the proposed Fair-SRS optimizes recommendations by making a trade-off between **accuracy** and **personalized diversity**.

# Demo link:

https://share.streamlit.io/ai-n/fair-srs-app/main/Fair_SRS_app.py

# Demo explanation

We build the demo dashboard of Fair-SRS on the sub-sample of Xing data using Streamlit (an open-source python framework for building web apps for ML and Data Science). 

This dashboard demonstrate Fair-SRS in three pages: (1)"**About Fair-SRS**", (2)"**Top-k recommendations**", and (3)"**Item Network**". 

     In the first page (**About Fair-SRS**), we explain the main framework of the proposed Fair-SRS model with a toy example. 

     In the second page (**Top-k recommendations**), all steps for generating top-k recommendations are shown including selecting a user, showing her historical and current sessions in both table and graph visualization, obtaining the results from DeepWalk model such as the similarity of items in current session and user's LID, highlighting the place of items in current session among the 2D visualization of items in the trained DeepWalk model, running the prediction model, evaluating and showing the results using evaluation metrics, and recommending top-5 items as user’s next click prediction. Any user can be selected via the slider in this page.

     Finally, in the third page (**Item Network**), the item network is visualized. It can be zoomed in and out so that people can click on nodes and see their connected items.
