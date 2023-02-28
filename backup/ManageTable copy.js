import React, { useState, useEffect } from "react";
import { getManageApplication } from './api';
import Paper from "@mui/material/Paper";
import TableRow from "@mui/material/TableRow";
import TableHead from "@mui/material/TableHead";
import TableBody from "@mui/material/TableBody"
import TableCell from "@mui/material/TableCell"
import Table from "@mui/material/Table";
import { withStyles } from "@mui/material";

const styles = thems =>({
    root : {
        width : '100%',
        marginTop : thems.spacing.unit * 3,
        overflowX: "auto"
    },
    table : {
        minWidth : 800
    }
})
const headerMeta = [
    "Name",
    "Employee Number",
    "Count",
    "Last Login",
];

function ManageTable() {
    // Update랑 조회 버튼 어디만들래
    // Table 아마 부트스트랩 써야할 것 같음
    const [tableData, setTableData] = useState([getManageApplication(1)]);
    
    const {classes} = styles;
        return (
            <Paper className={styles.root}>
                <Table className={styles.table}>
                    <TableHead>
                        <TableRow>
                            <TableCell>{headerMeta[0]}</TableCell>
                            <TableCell>{headerMeta[1]}</TableCell>
                            <TableCell>{headerMeta[2]}</TableCell>
                            <TableCell>{headerMeta[3]}</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {tableData[0].map((item,i) => {
                            console.log(item)
                        return (
                        <TableRow>
                            <TableCell key={i}>{item.application}</TableCell>
                            <TableCell>{item.instance}</TableCell>
                            <TableCell>{item.status}</TableCell>
                            <TableCell>{item.status2}</TableCell>
                        </TableRow>
                        );
                        })}
                    </TableBody>
                </Table>
            </Paper>
        );
    
}

export default ManageTable;