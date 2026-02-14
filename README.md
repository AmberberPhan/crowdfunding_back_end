# crowdfunding_back_end
Amber Phan

## Planning:
### Concept/Name: ThrvFd
Its a wellness and health-only crowdfunding platform where people create campaigns/fundraisers to improve their own (or someone else’s) physical/mental wellness and and only projects that genuinely improve well-being are approved.

### Intended Audience/User Stories
General User
As a user, I want to sign up and log in so my pledges and campaigns are tracked.
As a user, I want to browse wellness campaigns so I can discover causes that align with my values.
As a user, I want to view campaign progress and updates.

Creator (Campaign Owner)
As a creator, I want to create a fundraiser so I can raise pledges for a health or wellness goal.
As a creator, I want to be reviewed/approved before it goes live.
As a creator, I want to edit my campaign details.
As a creator, I want to close my fundraiser when it’s no longer accepting supporters.
As a creator, I want to delete my fundraiser if needed.


Supporter
As a supporter, I want to pledge to a fundraiser so I can help improve someone’s wellness.
As a supporter, I want to be prevented from pledging to a fundraiser that is closed.
As a supporter, I want my pledge history to be saved in my account.
As a supporter, I want to edit my pledge comment / anonymity if I change my mind.
As a supporter, I want to delete my pledge if needed.


Admin (superuser)
As an admin, I want to approve wellness fundraisers so only genuine wellbeing campaigns are visible publicly.

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

Home / Campaign Feed Page
 - View all approved wellness campaigns
 - Filter campaigns by category (e.g. Mental Health, Fitness, Nutrition)
 - Search campaigns by title or keyword
 - View campaign funding progress

Campaign Detail Page
 - View campaign description, goal amount, and current progress
 - View wellness category and campaign owner
 - Make a pledge to the campaign
 - View campaign updates

Create Campaign Page
 - Create a new wellness campaign
 - Add campaign title, description, wellness category, and funding goal
 - Submit campaign for approval
 - View campaign status (pending / approved / rejected)

User Dashboard
 - View campaigns I’ve created
 - View pledges I’ve made
 - Track campaign progress and funding totals


### API Spec
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |             |         |              |                       |                              |


| URL              | HTTP Method | Purpose                                                   | Request Body                                           | Success Response Code | Authentication/Authorisation    |
|------------------|-------------|-----------------------------------------------------------|--------------------------------------------------------|-----------------------|---------------------------------|
| /users/          | POST        | Register a new user                                       | { "username", "email", "password" }                    | 201 Created           | None                            |
| /api-token-auth/ | POST        | Get auth token + current user details                     | { "username", "password" }                             | 200 OK                | None                            |
| /fundraisers/    | POST        | Create a new fundraiser                                   | { "title", "description", "goal", "image", "is_open" } | 201 Created           | Auth required                   |
| /fundraisers/id/ | GET         | View a single fundraiser                                  | N/A                                                    | 200 OK                | None                            |
| /fundraisers/id/ | PUT/PATCH   | Update fundraiser (owner only)                            | { fields to update }                                   | 200 OK                | Auth (Owner only)               |
| /fundraisers/id/ | DELETE      | Delete fundraiser (owner only)                            | N/A                                                    | 204 No Content        | Auth (Owner only)               |
| /fundraisers/    | GET         | List all approved fundraisers                             | N/A                                                    | 200 OK                | None                            |
| /pledges/        | POST        | Create a pledge                                           | { "amount", "comment", "anonymous", "fundraiser" }     | 201 Created           | Auth required                   |
| /pledges/id/     | DELETE      | Delete a pledge (supporter only)                          | N/A                                                    | 204 No Content        | Auth (Supporter only)           |
| /pledges/{id}/   | PUT/PATCH   | Update pledge (comment + anonymous only) (supporter only) | { "comment": "", "anonymous": false }                  | 200 OK                | Token required + Supporter only |
| /pledges/{id}/   | DELETE      | Delete pledge (supporter only)                            | N/A                                                    | 204 No Content        | Token required + Supporter only |


### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )

### Link to Heroku: https://berber-04a1086dd4f2.herokuapp.com/users/


### Screenshots
GET request: https://ibb.co/nMgTWs3B

POST request: https://ibb.co/WvY3Nk9p

Token being returned: https://ibb.co/wDMJvRq

Step by step instructions for how to register a new user and create a new fundraiser (i.e. endpoints and body data);
