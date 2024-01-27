/** Updates the specified tables related links. */
function updateLinks(tableId, url, elements) {
    for (let x = 0; x < elements.length; x++) {
        const links = elements[x].getElementsByTagName('A');
        for (let y = 0; y < links.length; y++) {
            links[y].onclick = function(e) {
                e.preventDefault();
                url = buildUrl(url, decodeParameters(links[y].getAttribute('href')));
                updateTable(tableId, url);
            };
        }
    }
}

/** Updates the specified table and submits search queries. */
function updateTable(tableId, url, search=null) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE ) {
            if (xhr.status == 200) {
                // Replace the existing table with the table fetched from the request.
                var tableElement = document.getElementById(tableId);
                tableElement.innerHTML = xhr.responseText;

                // Update header column sort links.
                const headerElements = tableElement.getElementsByTagName('TH');
                updateLinks(tableId, url, headerElements);

                // Update page links.
                const paginationElements = tableElement.getElementsByTagName('pagination');
                updateLinks(tableId, url, paginationElements);
            }
        }
    };

    // If there is a search, add search parameters to our AJAX call.
    if (search) {
        let searchParam = {"search": search};
        url = buildUrl(url, searchParam);
    }
    xhr.open('GET', url, true);
    xhr.send();
}

/** Encodes a dictionary to a URL parameter string. */
function encodeParameters(params) {
    let result = '?';
    for (let i = 0; i < Object.keys(params).length; i++) {
        let currentKey = Object.keys(params).at(i)
        result += currentKey + "=" + params[currentKey];
        if (i < Object.keys(params).length - 1) {
            result += "&";
        }
    }
    return result;
}

/** Gets a dictionary of parameters from a given URL. */
function decodeParameters(url) {
    let result = {};
    let parameters = url.split("?");
    // No question mark, no parameters.
    if (parameters.length <= 1) return { };
    else parameters = parameters[1];
    parameters = parameters.split("&");
    // Iterate through each parameter key and value.
    for (i in parameters) {
        pair = parameters[i].split("=");
        if (pair.length == 2) {
            if (pair[1]) {
                result[pair[0]] = pair[1];
            }
        }
    }
    return result;
}

/** Removes all parameters from a given URL. */
function clearParameters(url) {
    split = url.split("?");
    if (split.length > 1) return split[0];
    else return url;
}

//** Appends parameters to a given URL. */
function buildUrl(url, params, keep_params=true) {
    let new_params = { };
    if (keep_params==true) new_params = decodeParameters(url);
    for (const [key, value] of Object.entries(params)) {
        new_params[key] = value;
    }
    return clearParameters(url) + encodeParameters(new_params);
}