var options = {
    data : categories,

    list: {
        maxNumberOfElements: 8,
        match: {
            enabled: true
        },
        sort: {
            enabled: true
        }
    },
};

$("#search_box").easyAutocomplete(options);
