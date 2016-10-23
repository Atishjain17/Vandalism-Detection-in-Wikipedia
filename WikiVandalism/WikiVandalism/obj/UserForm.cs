using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WikiVandalism
{
    public partial class UserForm : Form
    {
        public UserForm()
        {
            InitializeComponent();
            AutoCompleteStringCollection collection = new AutoCompleteStringCollection();
            var data = userTableAdapter1.GetData();

            foreach (var row in data)
            {
                collection.Add(row.username);
            }

            UserName.AutoCompleteCustomSource = collection;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MainForm f = new MainForm();
            this.Hide();
            f.Show();
        }

        private void SearchBtn_Click(object sender, EventArgs e)
        {
            string name = UserName.Text;

            userTableAdapter2.FillByUserName(vandalDBDataSet.User, name);
            userDataTableAdapter.FillByUserName(vandalDBDataSet.UserData, name);
            featuresTableAdapter.FillByUserName(vandalDBDataSet.Features, name);
        }

        private void featuresDataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void UserForm_Load(object sender, EventArgs e)
        {

        }

        private void featuresBindingSource_CurrentChanged(object sender, EventArgs e)
        {

        }

        private void bindingSource1_CurrentChanged(object sender, EventArgs e)
        {

        }


        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }



    }
}
