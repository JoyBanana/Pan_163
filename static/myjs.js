loadFileList();
function loadFileList() {
    fileList = new XMLHttpRequest();
    fileList.onreadystatechange = function () {
        if (fileList.readyState === 4 && fileList.status === 200) {
            list = JSON.parse(fileList.responseText);
            //console.log(list);
            for (let i = 0; i < list.length; i++) {
                add_table(list[i].Key,list[i].LastModified,list[i].Size);
            }
        }
    };
    fileList.open("GET", "/files", true);
    fileList.send();
}

function add_table(Name,Date,Size) {
    parent = document.getElementById("add_tr");
    div = document.createElement("tr");
    div.setAttribute("class", "success");
    parent.appendChild(div);

    fileName = document.createElement("td");
    fileName.setAttribute("width", "30%");
    fileName.setAttribute("align", "center");
    fileName.innerHTML = Name;
    div.appendChild(fileName);

    fileDate = document.createElement("td");
    fileDate.setAttribute("width", "25%");
    fileDate.setAttribute("align", "center");
    fileDate.innerHTML = Date;
    div.appendChild(fileDate);

    fileSize = document.createElement("td");
    fileSize.setAttribute("width", "25%");
    fileSize.setAttribute("align", "center");
    fileSize.innerHTML = Size;
    div.appendChild(fileSize);

    fileOpe = document.createElement("td");
    fileOpe.setAttribute("width", "20%");
    fileOpe.setAttribute("align", "center");
    div.appendChild(fileOpe);

    list4 = document.createElement("td");
    list4.setAttribute("type", "button");
    list4.setAttribute("class", "btn btn-default");
    list4.setAttribute("onclick", "window.open('https://joybanana.nos-eastchina1.126.net/" + fileName + "')");
    list4.innerHTML = "下载";
    fileOpe.appendChild(list4);


    <!--删除-->
    listform = document.createElement("form");
    listform.setAttribute("action", "/delete");
    listform.setAttribute("method", "post");
    fileOpe.appendChild(listform);


    listdel = document.createElement("td");
    listdel.setAttribute("type", "button");
    listdel.setAttribute("value", fileName);
    listdel.setAttribute("class", "btn btn-danger");
    listdel.innerHTML = "删除";
    listform.appendChild(listdel);

}