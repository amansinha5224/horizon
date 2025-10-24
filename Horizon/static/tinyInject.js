let script = document.createElement("script");
script.type = "text/javascript";
script.referrerPolicy = "origin";
script.src =
  "https://cdn.tiny.cloud/1/xhwultqs1bpv2e3u21w6byie3l9ret5d39v54a93hflzbogm/tinymce/8/tinymce.min.js";
document.head.append(script);

script.onload = function () {
  tinymce.init({
    selector: "#id_content",
    height: 600,
    plugins: [
      "advlist", "autolink", "link", "image", "lists", "charmap", "preview",
      "anchor", "pagebreak", "searchreplace", "wordcount", "visualblocks",
      "visualchars", "code", "fullscreen", "insertdatetime", "media",
      "table", "emoticons", "help"
    ],
    toolbar:
      "undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | " +
      "bullist numlist outdent indent | link image | print preview media fullscreen | " +
      "forecolor backcolor emoticons | help",
    menubar: "file edit view insert format tools table help",
    branding: false,
    promotion: false,
  });
};
