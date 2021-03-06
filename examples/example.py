from blockkit import Message, Section, Actions, MarkdownText, Button


message = Message(
    blocks=[
        Section(MarkdownText("You have a new request")),
        Section(
            fields=[
                MarkdownText("*Type:*\nComputer (laptop)"),
                MarkdownText("*When:*\nSubmitted Aut 10"),
                MarkdownText("*Last Update:*\nMar 10, 2015 (3 years, 5 months)"),
                MarkdownText("*Reason:*\nAll vowel keys aren't working."),
                MarkdownText("*Specs:*\nCheetah Pro 15 - Fast, really fast"),
            ],
        ),
        Actions(
            [
                Button("Approve", style=Button.primary, action_id="approve"),
                Button("Decline", style=Button.danger, action_id="decline"),
                Button("Discuss", action_id="discuss"),
            ]
        ),
    ]
)

message = message.build()
