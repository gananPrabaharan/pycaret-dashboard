import React from "react"
import {Type} from "react-bootstrap-table2-editor";

export const importTableColumns = [
    {
        dataField: "id",
        text: "Id",
        headerAlign: "center",
        hidden: true
    },
    {
        dataField: "name",
        text: "Feature Name",
        headerAlign: "center",
        sort: true
    },
    {
        dataField: "include",
        text: "Include Feature",
        type: "string",
        headerAlign: "center",
        sort: true,
        editable: true,
        editor: {
            type: Type.SELECT,
            options: [{
                value: "Yes",
                label: "Yes"
            }, {
                value: "No",
                label: "No"
            }]
        },
    }
];


export const createActionFormat = (actionFunction, buttonName) => {
    return (cell, row) => {
        return (
            <div>
                <button type="button" className="btn btn-outline-danger btn-sm ml-2 ts-buttom" size="sm"
                    onClick={() => {actionFunction(row)}}>
                    {buttonName}
                </button>
            </div>
        );
    }
}
