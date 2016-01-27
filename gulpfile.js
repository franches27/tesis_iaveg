// Generated on 2016-01-16 using generator-jadestyl v0.2.8
var pkg = require('./package.json'),
  gulp = require('gulp'),
  nib = require('nib')(),
  gutil = require('gulp-util'),
  plumber = require('gulp-plumber'),
  rimraf = require('gulp-rimraf'),
  rename = require('gulp-rename'),
  connect = require('gulp-connect'),
  browserify = require('gulp-browserify'),
  uglify = require('gulp-uglify'),
  stylus = require('gulp-stylus'),
  autoprefixer = require('gulp-autoprefixer'),
  csso = require('gulp-csso'),
  through = require('through'),
  opn = require('opn'),
  ghpages = require('gh-pages'),
  path = require('path'),
  htmlmin = require('gulp-htmlmin'),
  babel = require('gulp-babel'),
  isDist = process.argv.indexOf('serve') === -1;

gulp.task('js', ['clean:js'], function () {
  return gulp.src('src/scripts/main.js')
    .pipe(isDist ? through() : plumber())
    .pipe(browserify({ transform: ['debowerify'], debug: !isDist }))
    .pipe(isDist ? uglify() : through())
    .pipe(rename('build.js'))
    .pipe(gulp.dest('static/js'))
    .pipe(connect.reload());
});

gulp.task('babel', () => {
  return gulp.src('src/scripts/es2015/*.js')
    .pipe(babel({
      presets: ['es2015']
    }))
    .pipe(gulp.dest('src/scripts'));
});

gulp.task('css', ['clean:css'], function () {
  return gulp.src('src/styles/main.styl')
    .pipe(isDist ? through() : plumber())
    .pipe(stylus({
      // Allow CSS to be imported from node_modules and bower_components
      'include css': true,
      'compress':false,
      'paths': ['./node_modules','./src','./static/bower_components']
    }))
    .pipe(autoprefixer('last 2 versions', { map: false }))
    .pipe(isDist ? csso() : through())
    .pipe(rename('build.css'))
    .pipe(gulp.dest('static/build'))
    .pipe(connect.reload());
});

gulp.task('images', [], function () {
  return gulp.src('src/images/**/*.*')
    .pipe(gulp.dest('dist/images'))
    .pipe(connect.reload());
});

gulp.task('clean', function () {
  return gulp.src('dist')
    .pipe(rimraf());
});

gulp.task('clean:js', function () {
  return gulp.src('static/css/build.js')
    .pipe(rimraf());
});

gulp.task('clean:css', function () {
  return gulp.src('static/css/build.css')
    .pipe(rimraf());
});

gulp.task('connect', ['build'], function (done) {
  connect.server({
    root: 'dist',
    port: 80,
    livereload: true
  });
  opn('http://localhost:80', done);
});

gulp.task('watch', function () {
  gulp.watch('src/styles/**/*.styl', ['css']);
  gulp.watch('src/images/**/*', ['images']);
  gulp.watch('src/scripts/*.js', ['js']);
  gulp.watch('src/scripts/es2015/*.js', ['babel']);
});

gulp.task('deploy', ['build'], function (done) {
  ghpages.publish(path.join(__dirname, 'dist'), { logger: gutil.log }, done);
});

gulp.task('build', ['js', 'css', 'images']);
gulp.task('serve', ['connect', 'watch']);
gulp.task('default', ['build']);
