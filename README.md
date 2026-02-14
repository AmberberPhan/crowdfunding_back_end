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
As an admin, I want to view and approve wellness fundraisers so only genuine wellbeing campaigns are visible publicly.

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

| URL              | HTTP Method | Purpose                                                   | Request Body                                                    | Success Response Code | Authentication/Authorisation    |
|------------------|-------------|-----------------------------------------------------------|-----------------------------------------------------------------|-----------------------|---------------------------------|
| /users/          | POST        | Register a new user                                       | { "username", "email", "password" }                             | 201 Created           | None                            |
| /users/me/       | PUT/PATCH   | Update current user (username/email/password)             | Any of: { "username": "" }, { "email": "" }, { "password": "" } | 200 OK                | Auth required (self only)       |
| /users/me/       | DELETE      | Delete current user account                               | N/A                                                             | 204 No Content        | Auth required (self only)       |
| /api-token-auth/ | POST        | Get auth token + current user details                     | { "username", "password" }                                      | 200 OK                | None                            |
| /fundraisers/    | POST        | Create a new fundraiser                                   | { "title", "description", "goal", "image", "is_open" }          | 201 Created           | Auth required                   |
| /fundraisers/id/ | GET         | View a single fundraiser                                  | N/A                                                             | 200 OK                | None                            |
| /fundraisers/id/ | PUT/PATCH   | Update fundraiser (owner only)                            | { fields to update }                                            | 200 OK                | Auth (Owner only)               |
| /fundraisers/id/ | DELETE      | Delete fundraiser (owner only)                            | N/A                                                             | 204 No Content        | Auth (Owner only)               |
| /fundraisers/    | GET         | List all approved fundraisers                             | N/A                                                             | 200 OK                | None                            |
| /pledges/        | POST        | Create a pledge                                           | { "amount", "comment", "anonymous", "fundraiser" }              | 201 Created           | Auth required                   |
| /pledges/id/     | DELETE      | Delete a pledge (supporter only)                          | N/A                                                             | 204 No Content        | Auth (Supporter only)           |
| /pledges/id/     | PUT/PATCH   | Update pledge (comment + anonymous only) (supporter only) | { "comment": "", "anonymous": false }                           | 200 OK                | Token required + Supporter only |
| /pledges/id/     | DELETE      | Delete pledge (supporter only)                            | N/A                                                             | 204 No Content        | Token required + Supporter only |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )

### Link to Heroku: https://berber-04a1086dd4f2.herokuapp.com/users/


### Screenshots
GET request: https://ibb.co/nMgTWs3B

POST request: https://ibb.co/WvY3Nk9p

Token being returned: https://ibb.co/wDMJvRq

### Step by step instructions for how to register a new user and create a new fundraiser (i.e. endpoints and body data);

STEP 1: Register a new user

Endpoint: POST /users/

  "username": "Amber",
  "email": "abc@email.com",
  "password": "pass123"

Success response: 201 Created

STEP 2: Get an authentication token (log in)

Endpoint: POST /api-token-auth/

  "username": "Amber",
  "password": "passw123"

Success response: 200 OK
Example response (token):

  "token": "123454...",
  "user_id": 1,
  "email": "abc@email.com"

STEP 3 Create a fundraiser (must be logged in):

Endpoint: POST /fundraisers/
Authentication header:

Authorization: Token 123454...

Example request body (JSON):

  "title": "Mental Wellness Support",
  "description": "Raising funds for mental wellness support.",
  "goal": 500,
  "image": "https://example.com/image.jpg",
  "is_open": true


Success response: 201 Created
Notes:

owner is automatically set to the logged-in user.

is_approved defaults to false and must be approved in Django Admin before it appears in GET /fundraisers/

STEP 4: Approve the fundraiser in Django Admin (so it appears in the fundraiser list)

Go to: http://127.0.0.1:8000/admin/

Log in with superuser account.

Click Fundraisers.

Select the fundraiser you want to approve.

Set is_approved = True

Click Save. Then the fundraiser will appear when you call Endpoint: GET /fundraisers/