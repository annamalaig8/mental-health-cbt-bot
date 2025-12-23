import random

CBT_STAGES = {
    "reflect": {
        "negative_self": [
            "That sounds really painful to think about.",
            "I hear a lot of self-doubt in what you’re saying.",
            "It feels like you’re being very hard on yourself right now.",
            "That kind of thought can weigh heavily on anyone."
        ],
        "stress": [
            "That sounds stressful.",
            "It seems like there’s a lot of pressure on you.",
            "Anyone would feel overwhelmed in that situation.",
            "That’s a lot to carry at once."
        ],
        "focus": [
            "That sounds frustrating.",
            "Losing focus like that can be exhausting.",
            "It’s hard when your mind won’t cooperate.",
            "That can feel very draining."
        ],
        "positive": [
            "That’s good to hear.",
            "It sounds like something is going right.",
            "I’m glad you’re experiencing that.",
            "That’s a nice moment to notice."
        ],
        "neutral": [
            "I’m listening.",
            "Okay.",
            "I see.",
            "Got it."
        ]
    },

    "explore": {
        "negative_self": [
            "What made you start feeling this way about yourself?",
            "Did something specific happen that triggered this thought?",
            "How long have you been thinking like this?",
            "When do these thoughts usually show up?"
        ],
        "stress": [
            "What part of this is stressing you the most?",
            "Is it related to studies, deadlines, or expectations?",
            "What feels most urgent right now?",
            "What’s been weighing on your mind lately?"
        ],
        "focus": [
            "When do you notice your focus dropping the most?",
            "Is your mind distracted or feeling tired?",
            "What usually pulls your attention away?",
            "Has this been happening often?"
        ],
        "positive": [
            "What do you think helped this happen?",
            "What’s been working for you recently?",
            "How does this make you feel?",
            "What would help you keep this going?"
        ],
        "neutral": [
            "Do you want to talk more about it?",
            "What’s been on your mind?",
            "How do you feel about this?",
            "Would you like to share more?"
        ]
    },

    "reframe": {
        "negative_self": [
            "Let’s pause for a second — is this thought a fact or a feeling?",
            "If a friend said this about themselves, what would you tell them?",
            "What evidence supports this thought, and what challenges it?",
            "Could there be another way to look at this?"
        ],
        "stress": [
            "Would breaking this into smaller steps help?",
            "What’s one thing you can control right now?",
            "What’s one small step you could take today?",
            "Is everything equally urgent?"
        ],
        "focus": [
            "Would focusing on just one small task help?",
            "Could a short break help reset your focus?",
            "What usually helps you refocus, even a little?",
            "Have you tried changing your environment?"
        ],
        "positive": [
            "How can you build on this feeling?",
            "What can you do to keep this momentum?",
            "What does this say about your effort?",
            "How does it feel to acknowledge this?"
        ],
        "neutral": [
            "Thanks for sharing that.",
            "I appreciate you telling me.",
            "That makes sense.",
            "I’m here with you."
        ]
    },

    "checkin": {
        "negative_self": [
            "How are you feeling right now after talking about this?",
            "Does this conversation feel helpful?",
            "Would you like to keep talking or pause for now?",
            "Are these thoughts feeling any lighter?"
        ],
        "stress": [
            "How are you feeling at this moment?",
            "Does talking about it help a little?",
            "Would you like to continue or take a break?",
            "Do you feel slightly clearer now?"
        ],
        "focus": [
            "How are you feeling now?",
            "Does this feel useful?",
            "Want to keep going or pause?",
            "Is your mind feeling any calmer?"
        ],
        "positive": [
            "How does it feel to talk about this?",
            "Would you like to stay with this feeling?",
            "Anything else you want to share?",
            "Do you want to talk about something else?"
        ],
        "neutral": [
            "Do you want to continue?",
            "We can pause if you want.",
            "I’m here either way.",
            "Take your time."
        ]
    }
}

def get_response(label, stage):
    return random.choice(CBT_STAGES[stage][label])
