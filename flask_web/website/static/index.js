function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

// function goProfile(user,noteUserId) {
//   fetch("/go-profile",{
//     method:"GET",
//   })
//   // fetch("/go-profile", {
//   //   method: "GET",
//   //   body: JSON.stringify({ noteUserId: noteUserId }),
//   // }).then((_res) => {
//   //window.location.href = "/profile";
//   //});
// }
