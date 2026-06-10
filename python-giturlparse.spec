Name:           python-giturlparse
Version:        0.14.0
Release:        %autorelease
Summary:        Parse & rewrite git urls

License:        ASL
URL:            https://github.com/nephila/giturlparse
Source:         %{url}/archive/%{version}/giturlparse-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Parse & rewrite git urls (supports GitHub, Bitbucket, FriendCode, Assembla,
Gitlab ...) }

%description %_description

%package -n python3-giturlparse
Summary:        %{summary}

%description -n python3-giturlparse %_description


%prep
%autosetup -n giturlparse-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files giturlparse


%check
%tox


%files -n python3-giturlparse -f %{pyproject_files}
%doc README.*


%changelog
