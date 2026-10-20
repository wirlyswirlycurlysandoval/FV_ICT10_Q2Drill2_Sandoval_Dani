from pyscript import document, display

grade7_members = {
    "Deandre Faiyaz",
    "Nathania Parayno",
}

grade8_members = {
    "Samantha Bautista",
}

grade9_members = {
    "Inno Peña",
    "Chloe Adlawan",
    "Chelsi Sibal",
    "Aleynah Redillas",
    "Jillian Eusebio",
}

grade10_members = {
    "Erin Rioflorido",
    "Dani Sandoval",
    "Georgina Banal",
    "Lance Catu",
    "Sabine Agacita",
    "Mandy Cajanding",
    "Julia Bermudez"
}

all_members = (
    grade7_members
    | grade8_members
    | grade9_members
    | grade10_members
)

def add_member(e):
    global all_members

    first_name = document.getElementById("first").value.strip().title()
    last_name = document.getElementById("last").value.strip().title()
    #get and format the names that the user has entered

    new_member = f"{first_name} {last_name}".strip()
    #combine the first and last names

    all_members = all_members | {new_member}
     #use union operator to add the new member

    members_list = "<br>".join(sorted(all_members))
    #sort the members alphabetically
    
    members_list = len(all_members)
       #count total number of members

    document.getElementbyId("output2").innerHTML = f"""
    <h4>Club Member Directory</h4>
        <hr>
        <h5>Total Members: {total_members}</h5>
        <br>
        <div id="member-list">
            {members_list}
        </div>
    """
