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

$("#round").easyAutocomplete(options);
