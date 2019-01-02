loadFileList();
function loadFileList() {
    fileList = new XMLHttpRequest();
    fileList.onreadystatechange = function () {
        if (fileList.readyState === 4 && fileList.status === 200) {
            list = JSON.parse(fileList.responseText);
            //console.log(list);
            for (let i = 0; i < list.length; i++) {
                add_table(list[i]);
            }
        }
    };
    fileList.open("GET", "/files", true);
    fileList.send();
}

function add_table(fileName) {
    parent = document.getElementById("add_tr");
    div = document.createElement("tr");
    div.setAttribute("class", "success");
    parent.appendChild(div);

    list1 = document.createElement("td");
    list1.setAttribute("width", "50%");
    list1.setAttribute("align", "center");
    list1.innerHTML = fileName;
    div.appendChild(list1);

    list2 = document.createElement("td");
    list2.setAttribute("width", "30%");
    list2.setAttribute("align", "center");
    list2.innerHTML = "N/A";
    div.appendChild(list2);

    list3 = document.createElement("td");
    list3.setAttribute("width", "20%");
    list3.setAttribute("align", "center");
    div.appendChild(list3);

    list4 = document.createElement("td");
    list4.setAttribute("type", "button");
    list4.setAttribute("class", "btn btn-default");
    list4.setAttribute("onclick", "window.open('https://joybanana.nos-eastchina1.126.net/" + fileName + "')");
    list4.innerHTML = "下载";
    list3.appendChild(list4);

    listform = document.createElement("form");
    listform.setAttribute("action", "/delete");
    listform.setAttribute("method", "post");
    list3.appendChild(listform);


    listdel = document.createElement("td");
    listdel.setAttribute("type", "button");
    listdel.setAttribute("value", fileName);
    listdel.setAttribute("class", "btn btn-danger");
    listdel.innerHTML = "删除";
    listform.appendChild(listdel);

}