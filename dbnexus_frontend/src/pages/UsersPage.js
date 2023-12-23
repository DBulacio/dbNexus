import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { DataGrid, GridToolbarContainer, GridToolbarExport } from '@mui/x-data-grid';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';

const UsersPage = () => {
  const navigate = useNavigate();
  const [users, setUsers] = useState([]);
  const [rows, setRows] = useState([]);
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [selectedUserId, setSelectedUserId] = useState(null);

  const getUsers = async () => {
    let res = await fetch("/api/users/");
    let data = await res.json();

    setUsers(data);

    console.log('>>', data)

    let newRows = data.map(element => ({
      id: element.id,
      dni: element.dni,
      first_name: element.first_name,
      last_name: element.last_name,
    }));

    setRows(newRows);
  };

  useEffect(() => {
    getUsers();
  }, []);

  const deleteUser = async (id) => {
    await fetch(`/api/users/${id}/`, {
      method: "DELETE",
      headers: {
        'Content-Type': 'application/json'
      }
    });

    setDeleteDialogOpen(false);

    // refresh data after deletion
    getUsers();
  };

  const handleEdit = (params) => {
    const { id } = params.row;
    navigate(`update/${id}`);
  };

  const handleDelete = (id) => {
    setSelectedUserId(id);
    setDeleteDialogOpen(true);
  };

  const handleCloseDeleteDialog = () => {
    setDeleteDialogOpen(false);
  };

  const handleConfirmDelete = () => {
    deleteUser(selectedUserId);
  };

  const CustomToolbar = () => (
    <GridToolbarContainer>
      <Button
        color="primary"
        onClick={() => navigate("add")}
      >
        Add User
      </Button>
      <GridToolbarExport />
    </GridToolbarContainer>
  );

  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'first_name', headerName: 'First name', width: 150 },
    { field: 'last_name', headerName: 'Last name', width: 150 },
    // { field: 'dni', headerName: 'DNI', type: 'number', width: 90 },
    {
      field: 'action',
      headerName: 'Action',
      width: 160,
      renderCell: (params) => (
        <>
          <Button onClick={() => handleEdit(params)}>Update</Button>
          <Button onClick={() => handleDelete(params.row.id)} color="secondary">Delete</Button>
        </>
      ),
    },
  ];

  return (
    <>
      <div>
        <h1>Listado de usuarios</h1>
        <DataGrid
          sx={{width: 800}}
          rows={rows}
          columns={columns}
          pageSize={5}
          slots={{
            toolbar: CustomToolbar,
          }}
        />
      </div>
      <Dialog
        open={deleteDialogOpen}
        onClose={handleCloseDeleteDialog}
      >
        <DialogTitle>Delete User</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Are you sure you want to delete this user?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDeleteDialog}>Cancel</Button>
          <Button onClick={handleConfirmDelete} color="secondary">Delete</Button>
        </DialogActions>
      </Dialog>
    </>
  );
};

export default UsersPage;
