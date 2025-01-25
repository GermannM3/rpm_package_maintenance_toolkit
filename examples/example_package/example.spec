# examples/example_package/example.spec

Name: example_package
Version: 1.0
Release: 1
Summary: Example package with a script and a text file
License: MIT
Source0: example_package-%{version}.tar.gz
BuildArch: noarch

%description
This is an example package that includes a script and a text file.

%prep
%setup -q

%build
# В данном случае сборка не требуется, так как у нас только скрипт и текстовый файл

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 example_script.sh %{buildroot}/usr/local/bin/
install -m 644 some_file.txt %{buildroot}/usr/local/share/example_package/

%files
/usr/local/bin/example_script.sh
/usr/local/share/example_package/some_file.txt

%changelog
* Sat Jan 27 2024 Your Name <youremail@example.com> - 1.0-1
- Initial package
