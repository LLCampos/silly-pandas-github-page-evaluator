// function populateFirstUserInfo(user) {
//   populateFirstUserPersonalInfo(user);
//   populateFirstUserGeneralInfo(user);
// }

// function populateFirstUserPersonalInfo(user) {
//   $("#realname").text(user.user_realname);
//   $("#username").text(user.user_name);
//   $("#user_location").text(user.location)
//   $("#user_email").text(user.email)
//   $("#profile-pic img").attr('src', user.profile_pic_url)
//   $('#personal-user-info').toggleClass("hidden")
// }

// function populateFirstUserGeneralInfo(user) {
//   $("#number_pull_requests").text(user.number_of_pull_requests)
//   $("#number_issues").text(user.number_of_opened_issues)
//   $("#number_repos").text(user.number_of_repositories)
//   $('#general-user-info').toggleClass("hidden")
// }


// $().ready(($) => {

//   let examples_json = {
//       "user": {
//         "user_name": "LLCampos",
//         "user_realname": "Luís Campos",
//         "number_of_followers": 7,
//         "location": "Portugal",
//         "email": "luis1212@sapo.pt",
//         "profile_pic_url": "https://avatars2.githubusercontent.com/u/12008784?v=3&s=460",
//         "number_of_repositories": 56,
//         "number_of_pull_requests": 4,
//         "number_of_opened_issues": 5,
//         "languages": [
//             {"language_name": "Python",
//              "additions": 857,
//              "deletions": 560,
//              "number_of_commits": 67,
//              "number_of_repositories": 8,
//              "examples_repositories": [
//                 {"repository_name": "pybioportal",
//                  "url": "https://github.com/LLCampos/pybioportal"},
//                 {"repository_name": "blablabla",
//                  "url": "https://github.com/LLCampos/pybioportal"},
//              ]},
//             {"language_name": "Java",
//              "additions": 345,
//              "deletions": 987,
//              "number_of_commits": 67,
//              "number_of_repositories": 8,
//              "examples_repositories": [
//                 {"repository_name": "pybioportal",
//                  "url": "https://github.com/LLCampos/pybioportal"},
//                 {"repository_name": "blablabla",
//                  "url": "https://github.com/LLCampos/pybioportal"},
//              ]},
//         ]
//       }
//     }

//   $("#submit-profile-user").on('click', function(event) {
//     populateFirstUserInfo(examples_json.user);
//     event.preventDefault();
//   })


// });
