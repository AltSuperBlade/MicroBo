function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    // var fm = document.referrer;
    // window.alert(fm);
    // var wr = fm.charAt(fm.length - 1);
    // if (wr == "/") {
    window.location.href = "/";
    // } else {
    //   window.location.href = "/profile/" + wr;
    // }
  });
}
