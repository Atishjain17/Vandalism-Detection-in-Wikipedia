using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using WikiVandalism.Properties;

namespace WikiVandalism
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void TrainBtn_Click(object sender, EventArgs e)
        {
            TrainForm tf = new TrainForm();
            tf.Show();
            this.Hide();
        }

        private void UserBtn_Click(object sender, EventArgs e)
        {
            UserForm f = new UserForm();
            f.Show();
            this.Hide();
        }

        private void PageBtn_Click(object sender, EventArgs e)
        {
            PageForm f = new PageForm();
            f.Show();
            this.Hide();
        }

        public static string RunPythonScript(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();

            string pythonPath = Settings.Default.PythonPath;
            Console.WriteLine(pythonPath);

            if (pythonPath.Equals("--"))
            {
                OpenFileDialog openFileDialog1 = new OpenFileDialog();
                openFileDialog1.InitialDirectory = "c:\\";
                openFileDialog1.Filter = "Python Executable File (python.exe)|*.exe";
                openFileDialog1.FilterIndex = 1;
                openFileDialog1.RestoreDirectory = true;

                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    if (openFileDialog1.FileName.Contains("python.exe"))
                    {
                        pythonPath = openFileDialog1.FileName;
                        Settings.Default.PythonPath = pythonPath;
                        Settings.Default.Save();
                    }
                    else
                    {
                        MessageBox.Show("Python.exe is not chosen. Cannot execute python script.");
                        return "";
                    }
                }
                else
                {
                    return "";
                }
            }

            start.FileName = pythonPath;
            start.Arguments = ""+ cmd;
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    return result;
                }
            }
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            base.OnFormClosing(e);

            if (e.CloseReason == CloseReason.WindowsShutDown) return;

            // Confirm user wants to close
            switch (MessageBox.Show(this, "Are you sure you want to close?", "Closing", MessageBoxButtons.YesNo))
            {
                case DialogResult.No:
                    e.Cancel = true;
                    break;
                default:
                    break;
            }
        }
        
    }
}
