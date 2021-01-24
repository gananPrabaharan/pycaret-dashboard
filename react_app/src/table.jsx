import React from "react";
import BootstrapTable from "react-bootstrap-table-next";
import cellEditFactory from "react-bootstrap-table2-editor";
import paginationFactory from "react-bootstrap-table2-paginator";
import filterFactory from "react-bootstrap-table2-filter";
import './css/table.css'


const Table = (props) => {
    // Expects three prop values
    // dataList: List of data
    // columns: BootstrapTable columns list
    // changeStateData: Function to change parent dataList property

    const afterSaveCell = (oldValue, newValue, row, column) => {
        if (props.changeStateData != null){
            if (oldValue !== newValue){
                // Replace the changed row with new row
                for (var i=0; i<props.dataList.length; i++){
                    if (props.dataList[i].id === row.id){
                        props.dataList[i] = row;
                        break;
                    }
                }

                // Reset state with tempData
                props.changeStateData(props.dataList)
            }
        }
    };


    return(
        <div >
            <BootstrapTable
                bootstrap4
                noDataIndication="No Data Found"
                condensed
                // bordered
                // striped
                hover
                loading
                keyField="id"
                data={ props.dataList }
                columns={ props.columns }
                pagination={ paginationFactory({}) }
                cellEdit={ cellEditFactory({mode: "click", blurToSave: true,
                    afterSaveCell:(oldValue, newValue, row, column) => {afterSaveCell(oldValue, newValue, row, column)}
                }) }
                filter={ filterFactory() }
            />
        </div>
    )
}

export default Table