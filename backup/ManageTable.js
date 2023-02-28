import React, { useState, useEffect } from "react";
import { getManageApplication } from './api';
import TableRow from "@mui/material/TableRow";
import TableHead from "@mui/material/TableHead";
import TableBody from "@mui/material/TableBody"
import TableCell from "@mui/material/TableCell"
import Table from "@mui/material/Table";

import Tables from "./table";

const headerMeta = [
    "Instance",
    "App",
    "Status",
    "Blocked",
    "Stop",
];
const obj = {
    data2 :[
            {
              'application': "Dummy Data1",
              'instance': "Dummy Data",
              'status': "Dummy Data",
            },
            {
              'application': "Dummy Data2",
              'instance': "Dummy Data",
              'status': "Dummy Data",
            },{
              'application': "Dummy Data3",
              'instance': "Dummy Data",
              'status': "Dummy Data",
            }
          ]
      }

class ManageTable extends React.Component {
    // Update랑 조회 버튼 어디만들래
    // Table 아마 부트스트랩 써야할 것 같음

    render(){
        console.log(Object.values(this.props.lic))
        return (
            <div>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>{headerMeta[0]}</TableCell>
                            <TableCell>{headerMeta[1]}</TableCell>
                            <TableCell>{headerMeta[2]}</TableCell>
                            <TableCell>{headerMeta[3]}</TableCell>
                            <TableCell>{headerMeta[4]}</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {obj.data2.map((item) => {
                        return (
                        <TableRow>
                            <TableCell>{item.application}</TableCell>
                            <TableCell>{item.instance}</TableCell>
                            <TableCell>{item.instance}</TableCell>
                            <TableCell>{item.instance}</TableCell>
                            <TableCell>{item.instance}</TableCell>
                        </TableRow>
                        );
                        })}
                    </TableBody>
                </Table>
            </div>
        );
    }
}

export default ManageTable;