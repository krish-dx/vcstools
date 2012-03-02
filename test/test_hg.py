from vcstools.hg import HgClient


        subprocess.check_call("hg init", shell=True, cwd=remote_path)
        subprocess.check_call("touch fixed.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg add fixed.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg commit -m initial", shell=True, cwd=remote_path)
        po = subprocess.Popen("hg log --template '{node|short}' -l1", shell=True, cwd=remote_path, stdout=subprocess.PIPE)
        self.local_version_init = po.stdout.read().rstrip("'").lstrip("'")
        subprocess.check_call("hg tag test_tag", shell=True, cwd=remote_path)
        subprocess.check_call("touch modified.txt", shell=True, cwd=remote_path)
        subprocess.check_call("touch modified-fs.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg add modified.txt modified-fs.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg commit -m initial", shell=True, cwd=remote_path)
        po = subprocess.Popen("hg log --template '{node|short}' -l1", shell=True, cwd=remote_path, stdout=subprocess.PIPE)
        self.local_version_second = po.stdout.read().rstrip("'").lstrip("'")
        subprocess.check_call("touch deleted.txt", shell=True, cwd=remote_path)
        subprocess.check_call("touch deleted-fs.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg add deleted.txt deleted-fs.txt", shell=True, cwd=remote_path)
        subprocess.check_call("hg commit -m modified", shell=True, cwd=remote_path)
        po = subprocess.Popen("hg log --template '{node|short}' -l1", shell=True, cwd=remote_path, stdout=subprocess.PIPE)
        self.local_version = po.stdout.read().rstrip("'").lstrip("'")

        self.local_path = os.path.join(directory, "local")
        self.local_url = remote_path
    def tearDown(self):
        if os.path.exists(self.local_path):
            shutil.rmtree(self.local_path)

        url = self.local_url
        client = HgClient(self.local_path)
        client.checkout(url, self.local_version)
        self.assertEqual(client.get_url(), self.local_url)
        self.assertEqual(client.get_version(), self.local_version)
        self.assertEqual(client.get_version(self.local_version_init[0:6]), self.local_version_init)
        self.assertEqual(client.get_version("test_tag"), self.local_version_init)
        url = self.local_url
        client = HgClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        self.assertEqual(client.get_version(), self.local_version)

    def test_checkout_emptystringversion(self):
        # special test to check that version '' means the same as None
        url = self.local_url
        client = HgClient(self.local_path)
        self.assertTrue(client.checkout(url, ''))
        self.assertEqual(client.get_version(), self.local_version)
        
        local_path = os.path.join(self.local_path, "nonexistant_subdir")
        url = self.local_url
        url = self.local_url
        version = self.local_version
        client = HgClient(self.local_path)
        self.assertEqual(client.get_path(), self.local_path)
        new_version = self.local_version_second

        self.assertTrue(client.update())
        self.assertEqual(client.get_version(), self.local_version)

        self.assertTrue(client.update(new_version))
        self.assertEqual(client.get_version(), new_version)

        self.assertTrue(client.update(''))
        self.assertEqual(client.get_version(), self.local_version)
       
        url = self.local_url
        client = HgClient(self.local_path)
        client.checkout(url)
        # after setting up "local" repo, change files and make some changes
        subprocess.check_call("rm deleted-fs.txt", shell=True, cwd=self.local_path)
        subprocess.check_call("hg rm deleted.txt", shell=True, cwd=self.local_path)
        f = io.open(os.path.join(self.local_path, "modified.txt"), 'a')
        f = io.open(os.path.join(self.local_path, "modified-fs.txt"), 'a')
        f = io.open(os.path.join(self.local_path, "added-fs.txt"), 'w')
        f = io.open(os.path.join(self.local_path, "added.txt"), 'w')
        subprocess.check_call("hg add added.txt", shell=True, cwd=self.local_path)
    def tearDown(self):
        pass
        

        client = HgClient(self.local_path)

        client = HgClient(self.local_path)
        self.assertEquals('diff --git local/added.txt local/added.txt\nnew file mode 100644\n--- /dev/null\n+++ local/added.txt\n@@ -0,0 +1,1 @@\n+0123456789abcdef\n\\ No newline at end of file\ndiff --git local/deleted.txt local/deleted.txt\ndeleted file mode 100644\ndiff --git local/modified-fs.txt local/modified-fs.txt\n--- local/modified-fs.txt\n+++ local/modified-fs.txt\n@@ -0,0 +1,1 @@\n+0123456789abcdef\n\\ No newline at end of file\ndiff --git local/modified.txt local/modified.txt\n--- local/modified.txt\n+++ local/modified.txt\n@@ -0,0 +1,1 @@\n+0123456789abcdef\n\\ No newline at end of file\n\n', client.get_diff(basepath=os.path.dirname(self.local_path)))
        client = HgClient(self.local_path)
        client = HgClient(self.local_path)
        client = HgClient(self.local_path)
        self.assertEquals('M local/modified-fs.txt\nM local/modified.txt\nA local/added.txt\nR local/deleted.txt\n! local/deleted-fs.txt\n', client.get_status(basepath=os.path.dirname(self.local_path)))
        client = HgClient(self.local_path)