{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59117116-7e46-4883-bccf-746648cb6a59",
   "metadata": {},
   "outputs": [
    {
     "ename": "UnpicklingError",
     "evalue": "invalid load key, '{'.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnpicklingError\u001b[0m                           Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 7\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Load model\u001b[39;00m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlog_reg_model.pkl\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[1;32m----> 7\u001b[0m     model \u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(f)\n\u001b[0;32m      9\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTitanic Survival Prediction 🚢\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m# User inputs\u001b[39;00m\n",
      "\u001b[1;31mUnpicklingError\u001b[0m: invalid load key, '{'."
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Load model\n",
    "with open(\"log_reg_model.pkl\", \"rb\") as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "st.title(\"Titanic Survival Prediction 🚢\")\n",
    "\n",
    "# User inputs\n",
    "pclass = st.selectbox(\"Passenger Class\", [1,2,3])\n",
    "sex = st.selectbox(\"Sex\", [\"male\", \"female\"])\n",
    "age = st.slider(\"Age\", 0, 80, 25)\n",
    "sibsp = st.number_input(\"Siblings/Spouses aboard\", 0, 10, 0)\n",
    "parch = st.number_input(\"Parents/Children aboard\", 0, 10, 0)\n",
    "fare = st.number_input(\"Fare\", 0.0, 600.0, 32.0)\n",
    "embarked = st.selectbox(\"Embarked\", [\"S\", \"C\", \"Q\"])\n",
    "\n",
    "# Encode inputs\n",
    "sex_map = {\"male\":0, \"female\":1}\n",
    "embarked_map = {\"S\":0, \"C\":1, \"Q\":2}\n",
    "\n",
    "input_data = pd.DataFrame({\n",
    "    \"Pclass\":[pclass],\n",
    "    \"Sex\":[sex_map[sex]],\n",
    "    \"Age\":[age],\n",
    "    \"SibSp\":[sibsp],\n",
    "    \"Parch\":[parch],\n",
    "    \"Fare\":[fare],\n",
    "    \"Embarked\":[embarked_map[embarked]]\n",
    "})\n",
    "\n",
    "if st.button(\"Predict Survival\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    if prediction == 1:\n",
    "        st.success(\"🎉 This passenger would have SURVIVED!\")\n",
    "    else:\n",
    "        st.error(\"💀 This passenger would NOT have survived.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "782a658e-c465-41d1-b393-eeb49fb179a8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
