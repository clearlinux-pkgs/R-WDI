#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-WDI
Version  : 2.6.0
Release  : 11
URL      : https://cran.r-project.org/src/contrib/WDI_2.6.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/WDI_2.6.0.tar.gz
Summary  : World Development Indicators (World Bank)
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-RJSONIO
BuildRequires : buildreq-R

%description
World Development Indicators.

%prep
%setup -q -c -n WDI

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552919583

%install
export SOURCE_DATE_EPOCH=1552919583
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WDI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WDI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library WDI
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  WDI || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/WDI/DESCRIPTION
/usr/lib64/R/library/WDI/INDEX
/usr/lib64/R/library/WDI/Meta/Rd.rds
/usr/lib64/R/library/WDI/Meta/data.rds
/usr/lib64/R/library/WDI/Meta/features.rds
/usr/lib64/R/library/WDI/Meta/hsearch.rds
/usr/lib64/R/library/WDI/Meta/links.rds
/usr/lib64/R/library/WDI/Meta/nsInfo.rds
/usr/lib64/R/library/WDI/Meta/package.rds
/usr/lib64/R/library/WDI/NAMESPACE
/usr/lib64/R/library/WDI/NEWS
/usr/lib64/R/library/WDI/R/WDI
/usr/lib64/R/library/WDI/R/WDI.rdb
/usr/lib64/R/library/WDI/R/WDI.rdx
/usr/lib64/R/library/WDI/data/Rdata.rdb
/usr/lib64/R/library/WDI/data/Rdata.rds
/usr/lib64/R/library/WDI/data/Rdata.rdx
/usr/lib64/R/library/WDI/help/AnIndex
/usr/lib64/R/library/WDI/help/WDI.rdb
/usr/lib64/R/library/WDI/help/WDI.rdx
/usr/lib64/R/library/WDI/help/aliases.rds
/usr/lib64/R/library/WDI/help/paths.rds
/usr/lib64/R/library/WDI/html/00Index.html
/usr/lib64/R/library/WDI/html/R.css
