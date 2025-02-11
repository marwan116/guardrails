# flake8: noqa: E501
VALIDATED_OUTPUT_SKELETON_REASK_2 = {
    "fees": [
        {"name": "annual_membership_fee", "explanation": "", "value": 0.0},
        {"name": "my_chase_plan_fee", "explanation": "", "value": 1.72},
        {"name": "balance_transfers", "explanation": "", "value": 5.0},
        {"name": "cash_advances", "explanation": "", "value": 5.0},
        {"name": "foreign_transactions", "explanation": "", "value": 3.0},
        {"name": "late_payment", "explanation": "", "value": 0.0},
        {"name": "over-the-credit-limit", "explanation": "", "value": 0.0},
        {"name": "return_payment", "explanation": "", "value": 0.0},
        {"name": "return_check", "explanation": "", "value": 0.0},
    ],
    "interest_rates": {
        "purchase": {
            "annual_percentage_rate": 0.0,
            "variation_explanation": "This APR will vary with the market based on the Prime Rate.",
        },
        "balance_transfer": {
            "annual_percentage_rate": 0.0,
            "variation_explanation": "This APR will vary with the market based on the Prime Rate.",
        },
        "cash_advance": {
            "annual_percentage_rate": 29.49,
            "variation_explanation": "This APR will vary with the market based on the Prime Rate.",
        },
        "penalty": {
            "annual_percentage_rate": 29.99,
            "variation_explanation": "This APR will vary with the market based on the Prime Rate.",
            "when_applies": "We may apply the Penalty APR to your account if you: fail to make a Minimum Payment by the date and time that it is due; or make a payment to us that is returned unpaid.",
            "how_long_apr_applies": "If we apply the Penalty APR for either of these reasons, the Penalty APR could potentially remain in effect indefinitely.",
        },
    },
}
